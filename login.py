from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector


class LoginPage(BoxLayout, Screen):
    def check_credentials(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="study_appdb"
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        row = cursor.fetchone()

        if row:
            self.manager.current = 'dashboard'
        else:
            popup = Popup(title='Invalid Credentials', content=Label(text='Invalid username or password'),
                          size_hint=(None, None), size=(200, 100))
            popup.open()

        db.close()


class DashboardScreen(Screen):
    pass


class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm


if __name__ == '__main__':
    LoginApp().run()
