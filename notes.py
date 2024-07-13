from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os
import datetime


class NoteTextInput(TextInput):
    pass


class NoteListPage(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super(NoteListPage, self).__init__(**kwargs)
        self.documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')

    def on_enter(self):
        Clock.schedule_once(self.load_notes)

    def load_notes(self, dt=None):
        self.ids.note_list.clear_widgets()

        for filename in os.listdir(self.documents_dir):
            if filename.endswith(".txt"):
                note_button = Button(text=filename, size_hint_y=None, height=40)
                note_button.bind(on_press=self.open_note)
                self.ids.note_list.add_widget(note_button)

    def open_note(self, instance):
        filename = instance.text
        file_path = os.path.join(self.documents_dir, filename)
        with open(file_path, 'r') as file:
            note_text = file.read()
        self.ids.note_text_input.text = note_text


class NotePage(BoxLayout, Screen):
    def save_note(self, instance):
        note_text = self.ids.note_text_input.text
        current_datetime = datetime.datetime.now()
        filename = f"Note {current_datetime.strftime('%Y-%m-%d %H-%M-%S')}.txt"
        documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')

        if not os.path.exists(documents_dir):
            os.makedirs(documents_dir)

        file_path = os.path.join(documents_dir, filename)

        with open(file_path, 'w') as file:
            file.write(note_text)

        print(f"Note saved to {file_path}")


class NoteApp(App):
    def build(self):
        self.note_page = NotePage(name='note')
        self.note_list_page = NoteListPage(name='note_list')
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(self.note_page)
        self.screen_manager.add_widget(self.note_list_page)
        return self.screen_manager


if __name__ == '__main__':
    NoteApp().run()
