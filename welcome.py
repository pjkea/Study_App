from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from dashboard import DashboardScreen
from login import LoginPage
from signup import SignUpPage
from notes import NoteListPage, NotePage
from files import FileManagerScreen
from timetable import TimetableScreen


class WelcomeScreen(Screen):
    pass


class SignUpPage(Screen):
    pass


class LoginPage(Screen):
    pass


class DashboardScreen(Screen):
    pass


class NoteListPage(Screen):
    pass


class NotePage(Screen):
    pass


class FileManagerScreen(Screen):
    pass


class TimeTableScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class Welcome(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(SignUpPage(name='signup'))
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(NoteListPage(name='note_list'))
        sm.add_widget(NotePage(name='notes'))
        sm.add_widget(FileManagerScreen(name='files'))
        sm.add_widget(TimetableScreen(name='timetable'))  # Add the TimetableScreen to the ScreenManager
        sm.current = 'welcome'  # Set the current screen to 'welcome'
        return sm


if __name__ == '__main__':
    Welcome().run()
