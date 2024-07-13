from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from notes import NotePage, NoteListPage


class DashboardScreen(BoxLayout, Screen):
    pass


class DashBoard(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.dashboard_screen = DashboardScreen(name='dashboard')
        self.note_page = NotePage(name='note')
        self.note_list_page = NoteListPage(name='note_list')

        self.screen_manager.add_widget(self.dashboard_screen)
        self.screen_manager.add_widget(self.note_page)
        self.screen_manager.add_widget(self.note_list_page)
        return self.screen_manager



if __name__ == '__main__':
    DashBoard().run()
