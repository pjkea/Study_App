from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from dashboard import DashboardScreen
import mysql.connector


class DashboardScreen(Screen):
    pass


class SignUpPage(BoxLayout, Screen):
    def sign_up(self, username, password, year, course):
        print("Sign up method called")
        print("Manager:", self.manager)
        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="study_appdb"
        )
        cursor = db.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                 username VARCHAR(255),
                                 password VARCHAR(255),
                                 year VARCHAR(255),
                                 course VARCHAR(255)
                             )''')

        # Insert user data into the table
        cursor.execute("INSERT INTO users (username, password, year, course) VALUES (%s, %s, %s, %s)",
                       (username, password, year, course))
        db.commit()
        db.close()

        # Switch to dashboard screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'dashboard'


class SignUpApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignUpPage(name='signup'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm


if __name__ == '__main__':
    SignUpApp().run()
