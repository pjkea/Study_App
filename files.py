from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Load the kv file
Builder.load_file('files.kv')


class FileManagerScreen(Screen):
    def __init__(self, **kwargs):
        super(FileManagerScreen, self).__init__(**kwargs)

    def open_file_manager(self):
        # Create FileChooserListView instance
        file_chooser = FileChooserListView()

        # Bind the selection event
        file_chooser.bind(on_submit=self.file_selected)

        # Open file chooser as a popup
        self.popup = Popup(title="Choose a file", content=file_chooser, size_hint=(0.9, 0.9))
        self.popup.open()

    def file_selected(self, instance, selection, touch):
        # Close the popup
        self.popup.dismiss()

        # Display the selected file path in the label
        if selection:
            self.ids.selected_file_label.text = f'Selected file: {selection[0]}'


class FileManagerApp(App):
    def build(self):
        return FileManagerScreen()


if __name__ == '__main__':
    FileManagerApp().run()
