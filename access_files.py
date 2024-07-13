#main.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class NotesPage(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return NotesPage()

if __name__ == '__main__':
    MyApp().run()

#notes_page.kv

# <NotesPage>:
#     orientation: 'vertical'
#     padding: 20
#     spacing: 10
#
#     Label:
#         text: 'Notes and Resources'
#         font_size: 24
#         bold: True
#
#     BoxLayout:
#         orientation: 'horizontal'
#         size_hint_y: None
#         height: 40
#
#         Button:
#             text: 'Notes'
#             on_press: root.open_notes()
#
#         Button:
#             text: 'Slides'
#             on_press: root.open_slides()
#
#         Button:
#             text: 'Videos'
#             on_press: root.open_videos()
#
#     FileChooserListView:
#         id: file_chooser
#         path: '/path/to/files'

#NotesPage


class NotesPage(BoxLayout):
    def open_notes(self):
        file_path = self.ids.file_chooser.path + '/notes.txt'
        with open(file_path, 'r') as f:
            notes_text = f.read()
        self.show_notes(notes_text)

    def open_slides(self):
        file_path = self.ids.file_chooser.path + '/slides.pdf'
        # Open the slides file using a PDF viewer
        import webbrowser
        webbrowser.open(file_path)

    def open_videos(self):
        file_path = self.ids.file_chooser.path + '/video.mp4'
        # Open the video file using a video player
        import webbrowser
        webbrowser.open(file_path)

    def show_notes(self, notes_text):
        # Create a popup to display the notes
        popup = Popup(title='Notes', content=Label(text=notes_text), size_hint=(None, None), size=(400, 400))
        popup.open()

