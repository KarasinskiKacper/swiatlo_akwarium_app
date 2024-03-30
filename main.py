from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from main_page import MainPage
from second_page import SecondPage

class MyApp(App):
    def build(self):
        # Create a screen manager
        sm = ScreenManager()
        
        # Create the main page
        main_page = MainPage(name='main')
        sm.add_widget(main_page)
        
        # Create the second page
        second_page = SecondPage(name='second')
        sm.add_widget(second_page)
        
        return sm

if __name__ == '__main__':
    MyApp().run()
