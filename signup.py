from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.app import App


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
        return SignUpPage()


if __name__ == '__main__':
    SignUpApp().run()
