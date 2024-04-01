from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

import requests

SERVER = "http://192.168.1.61"

class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        
        # Create a layout for buttons
        layout = RelativeLayout()
        
        # Create four buttons
        button_height = 60
        button_width = 300
        button_spacing = 16
        
        button = Button(
            text="RESET CZASU", 
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(0, 1, 0, 1), 
            pos_hint={'center_x': 0.5, 'center_y': 1 - (1)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.reset_time)
        layout.add_widget(button) 

        button = Button(
            text=f'WŁĄCZ / WYŁĄCZ ŚWIATŁO', 
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 0, 0, 1),
            pos_hint={'center_x': 0.5, 'center_y': 1 - (2)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.switch_to_second_page)
        layout.add_widget(button)

        button = Button(
            text=f'Button 3', 
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 0, 0, 1),  # Red color
            pos_hint={'center_x': 0.5, 'center_y': 1 - (3)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(button)
        
        button = Button(
            text=f'Button 4', 
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 0, 0, 1),  # Red color
            pos_hint={'center_x': 0.5, 'center_y': 1 - (4)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(button)
        
        self.add_widget(layout)
        try:
            res = requests.get(SERVER + "/date", timeout=2.50).text
        except:
            res = "500"
        self.label = Label(
            text=res,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},  # Start label below the screen
        )
        layout.add_widget(self.label)
        
        # return layout
    
    def reset_time(self, instance):
        try:
            res = requests.get(SERVER + "", timeout=2.5).text
        except:
            res = "500"
        self.label.text = res
    
    def switch_to_second_page(self, instance):
        self.parent.current = 'second'
