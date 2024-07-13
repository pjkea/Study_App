from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class WelcomeScreen(BoxLayout, Screen):
    pass


class SignUpPage(BoxLayout, Screen):
    def sign_up(self, username, password, year, course):
        # Your sign-up logic here
        self.manager.transition.direction = 'left'
        self.manager.current = 'dashboard'


class DashboardScreen(BoxLayout, Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    MyApp().run()
