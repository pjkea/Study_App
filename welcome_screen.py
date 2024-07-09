from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Header
        header_label = Label(text='Welcome to [App Name]', font_size=24, color=(0, 0, 0, 1))
        self.add_widget(header_label)

        # Buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=20)
        sign_up_button = Button(text='Sign Up', background_color=(0, 0.7, 0, 1), color=(1, 1, 1, 1), font_size=18)
        login_button = Button(text='Login', background_color=(0, 0.4, 0.8, 1), color=(1, 1, 1, 1), font_size=18)
        button_layout.add_widget(sign_up_button)
        button_layout.add_widget(login_button)
        self.add_widget(button_layout)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()