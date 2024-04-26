from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

import requests

SERVER = "http://192.168.1.60"

SCALE = 4
class MainPage(Screen):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        
        # Create a layout for buttons
        layout = RelativeLayout()
        
        # Create four buttons
        button_height = 250 #/SCALE
        button_width = 900  #/SCALE
        button_spacing = 128#/SCALE
        font_size = 68     #/SCALE
        
        button = Button(
            text="TRYB AUTO", 
            font_size = font_size,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 1, 0, 1), 
            pos_hint={'center_x': 0.5, 'center_y': 1 - (1)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.auto)
        layout.add_widget(button) 

        button = Button(
            text=f'WŁĄCZ / WYŁĄCZ ŚWIATŁO', 
            font_size = font_size,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 0, 0, 1),
            pos_hint={'center_x': 0.5, 'center_y': 1 - (2)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.switch_to_second_page)
        layout.add_widget(button)

        # button = Button(
        #     text=f'Button 3', 
        #     size_hint=(None, None), 
        #     size=(button_width, button_height), 
        #     background_color=(1, 0, 0, 1),  # Red color
        #     pos_hint={'center_x': 0.5, 'center_y': 1 - (3)*((button_height + button_spacing) / Window.height)}
        # )
        # layout.add_widget(button)
        
        button = Button(
            text=f'ZMIANA KOLORU', 
            font_size = font_size,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(0, 0, 1, 1),  
            pos_hint={'center_x': 0.5, 'center_y': 1 - (3)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.tap)
        layout.add_widget(button)
        
        self.add_widget(layout)
        try:
            res = requests.get(SERVER + "/date", timeout=2.5).text
        except:
            res = "Błąd połączenia\nz mikrokontrolerem."
        self.label = Label(
            text=res,
            font_size = font_size,
            size_hint=(None, None),
            size=(200, 50),
            halign = 'center',
            pos_hint={'center_x': 0.5, 'y': 0.1},  # Start label below the screen
        )
        layout.add_widget(self.label)
        
        # return layout
    
    def auto(self, instance):
        try:
            requests.get(SERVER + "/auto", timeout=2.5)
            res = "Przywrócono tryb automatyczny"
        except:
            res = "500"
        self.label.text = res
    def tap(self, instance):
        try:
            requests.get(SERVER + "/relaytap", timeout=2.5)
            res = "Światło powinno zmienić kolor"
        except:
            res = "500"
        self.label.text = res
    
    def switch_to_second_page(self, instance):
        self.parent.current = 'second'
