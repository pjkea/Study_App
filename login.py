from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Create labels and input fields
        self.username_label = Label(text='Username:')
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)

        self.password_label = Label(text='Password:')
        self.password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)

        # Create login button
        self.login_button = Button(text='Login', background_color=(0, 0, 1, 1))
        self.login_button.size_hint_y = None
        self.login_button.height = 40
        self.add_widget(self.login_button)


class LoginApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    LoginApp().run()
