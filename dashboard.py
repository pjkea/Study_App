from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from notes import NotePage, NoteListPage
from timetable import TimetableScreen
from files import FileManagerScreen
from aichat import AiChatScreen


class DashboardScreen(BoxLayout, Screen):
    pass


class DashBoard(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.dashboard_screen = DashboardScreen(name='dashboard')
        self.note_page = NotePage(name='notes')
        self.note_list_page = NoteListPage(name='note_list')
        self.timetable = TimetableScreen(name='timetable')
        self.file_manager = FileManagerScreen(name='files')
        self.ai_chat = AiChatScreen(name='chat')

        self.screen_manager.add_widget(self.dashboard_screen)
        self.screen_manager.add_widget(self.note_page)
        self.screen_manager.add_widget(self.note_list_page)
        self.screen_manager.add_widget(self.timetable)
        self.screen_manager.add_widget(self.file_manager)
        self.screen_manager.add_widget(self.ai_chat)
        return self.screen_manager



if __name__ == '__main__':
    DashBoard().run()
