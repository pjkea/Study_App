#main.py
# main.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class AskAIScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class TheWatcherApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('thewatcher.kv')

if __name__ == '__main__':
    TheWatcherApp().run()



# thewatcher.kv


#main.py (Update with AI integration)
# main.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import openai

openai.api_key = 'your_openai_api_key'

class AskAIScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class TheWatcherApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('thewatcher.kv')

    def ask_ai(self, question):
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        self.root.get_screen('ask_ai').ids.response_label.text = answer

if __name__ == '__main__':
    TheWatcherApp().run()



#ai_integration.py If you prefer to keep the AI integration logic in a separate file, you can do so.

# ai_integration.py
import openai

openai.api_key = 'your_openai_api_key'

def ask_ai(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

#Update main.py to import and use this function
# main.py
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from ai_integration import ask_ai as ask_ai_integration

class AskAIScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class TheWatcherApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('thewatcher.kv')

    def ask_ai(self, question):
        answer = ask_ai_integration(question)
        self.root.get_screen('ask_ai').ids.response_label.text = answer

if __name__ == '__main__':
    TheWatcherApp().run()
