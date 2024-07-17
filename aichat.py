import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


# Mock Groq class with a query method
class Groq:
    def __init__(self, api_key):
        self.api_key = api_key

    def query(self, question):
        # Mock response for demonstration purposes
        return "This is a mock response to your question."


# Load the kv file
Builder.load_file('aichat.kv')


class AiChatScreen(Screen):
    def __init__(self, **kwargs):
        super(AiChatScreen, self).__init__(**kwargs)
        self.history_groups = {}  # Dictionary to store history groups
        self.history = []  # Current conversation history
        self.current_group = None  # Current chat group

        # Initialize Groq API
        groq_api_key = os.environ.get("GROQ_API_KEY")
        self.groq_client = Groq(api_key=groq_api_key)

    def new_chat(self):
        # Create a new history group
        if self.history:
            group_name = f'Chat {len(self.history_groups) + 1}'
            self.history_groups[group_name] = self.history.copy()
            self.history = []  # Clear current conversation history
            self.update_history_panel()

    def ask_question(self):
        question = self.ids.input_area.text.strip()
        if question:
            # Display the question
            self.add_message(f'You: {question}', 'left')
            self.history.append(f'You: {question}')
            self.ids.input_area.text = ''  # Clear the input area

            # Get response using Groq API
            response = self.get_groq_response(question)
            self.add_message(f'WATCHER: {response}', 'right')
            self.history.append(f'WATCHER: {response}')

    def add_message(self, message, side):
        label = Label(text=message, size_hint_y=None, padding=(10, 10),
                      text_size=(self.width * 0.9, None))
        label.bind(texture_size=label.setter('size'))
        label.halign = 'left' if side == 'left' else 'right'
        if side == 'right':
            with label.canvas.before:
                Color(0.8, 0.8, 1, 1)  # Light blue for AI messages
                Rectangle(size=label.size, pos=label.pos)
        self.ids.response_layout.add_widget(label)
        self.ids.response_area.scroll_y = 0  # Scroll to the bottom

    def get_groq_response(self, question):
        # Use Groq API to get response
        response = self.groq_client.query(question)
        return response

    def update_history_panel(self):
        # Update the history panel with the new history groups
        self.ids.history_list_layout.clear_widgets()
        for group_name, history in self.history_groups.items():
            group_button = ToggleButton(text=group_name, size_hint_y=None, height=40)
            group_button.bind(on_state=self.show_history_group)
            self.ids.history_list_layout.add_widget(group_button)

    def show_history_group(self, instance, value):
        if value == 'down':  # Button is pressed
            # Clear the response area
            self.ids.response_layout.clear_widgets()

            # Show the chat group
            group_name = instance.text
            self.current_group = group_name
            self.history = self.history_groups[group_name]
            for message in self.history:
                side = 'left' if message.startswith('You:') else 'right'
                self.add_message(message, side)


class AiChatApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AiChatScreen(name='aichat'))
        return sm


if __name__ == '__main__':
    AiChatApp().run()
