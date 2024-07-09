from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SignInPage(BoxLayout):
    def __init__(self, **kwargs):
        super(SignInPage, self).__init__(**kwargs)
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

        self.year_label = Label(text='Year:')
        self.year_input = TextInput(multiline=False)
        self.add_widget(self.year_label)
        self.add_widget(self.year_input)

        self.program_label = Label(text='Program:')
        self.program_input = TextInput(multiline=False)
        self.add_widget(self.program_label)
        self.add_widget(self.program_input)

        # Create submit button
        self.submit_button = Button(text='Submit', background_color=(0, 0, 1, 1))
        self.submit_button.size_hint_y = None
        self.submit_button.height = 40
        self.add_widget(self.submit_button)


class SignInApp(App):
    def build(self):
        return SignInPage()


if __name__ == '__main__':
    SignInApp().run()
