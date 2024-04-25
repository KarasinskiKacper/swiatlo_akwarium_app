from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window

import requests

SERVER = "http://192.168.0.115"

class My_TextInput1(TextInput):
    def __init__(self, **kwargs):
        super(My_TextInput1, self).__init__(**kwargs) 

    def on_text(self, instance, text: str):
        if len(text):
            if text[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.text = text[:-1]
            else:
                if len(text)>=2:
                    self.text = text[:2]
                    self.focus = False
                    self.next.focus = True
                if int(text)>23:
                    self.text = '23'
                
class My_TextInput2(TextInput):
    def __init__(self, **kwargs):
        super(My_TextInput2, self).__init__(**kwargs) 

    def on_text(self, instance, text: str):
        if len(text):
            if text[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.text = text[:-1]
            else:
                if len(text)>=2:
                    self.text = text[:2]
                    self.focus = False
                if int(text)>59:
                    self.text = '59'

class SecondPage(Screen):
    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)
        # self.add_widget(SecondPageHandler())
        layout = RelativeLayout()
        
        # Create four buttons
        button_height = 60
        button_width = 300
        button_spacing = 16

        label = Label(
            text=f'DO GODZINY:', 
            font_size = button_height,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            pos_hint={'center_x': 0.5, 'center_y': 1 - (1)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(label)
        
        self.input_box1 = My_TextInput1(
            multiline=False, 
            font_size = button_height/2,
            size_hint=(None, None), 
            size=(button_width/3, button_height), 
            pos_hint={'center_x': 0.42, 'center_y': 1 - (2)*((button_height + button_spacing) / Window.height)},
            halign = 'center',
            padding_y = [button_height / 2 - (button_height / 4), 0],
            text = ''
        )
        layout.add_widget(self.input_box1)
        label = Label(
            text=f':', 
            font_size = button_height,
            pos_hint={'center_x': 0.5, 'center_y': 1 - (2)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(label)
        self.input_box2 = My_TextInput2(
            multiline=False, 
            font_size = button_height/2,
            size_hint=(None, None), 
            size=(button_width/3, button_height), 
            pos_hint={'center_x': 0.58, 'center_y': 1 - (2)*((button_height + button_spacing) / Window.height)},
            halign = 'center',
            padding_y = [button_height / 2 - (button_height / 4), 0],
            text = ''
        )
        self.input_box1.next = self.input_box2
        layout.add_widget(self.input_box2)

        button = Button(
            text=f'ON', 
            size_hint=(None, None), 
            size=(button_width/2, button_height), 
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5 - (button_width/4/Window.width), 'center_y': 1 - (3)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.req_forserelayto_on)
        layout.add_widget(button)
        
        button = Button(
            text=f'OFF', 
            size_hint=(None, None), 
            size=(button_width/2, button_height), 
            background_color=(1, 0, 0, 1), 
            pos_hint={'center_x': 0.5 + (button_width/4/Window.width), 'center_y': 1 - (3)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(button)

        label = Label(
            text=f'NA STAŁE:', 
            font_size = button_height,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            pos_hint={'center_x': 0.5, 'center_y': 1 - (4)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(label)
        
        button = Button(
            text=f'ON', 
            size_hint=(None, None), 
            size=(button_width/2, button_height), 
            background_color=(0, 1, 0, 1),
            pos_hint={'center_x': 0.5 - (button_width/4/Window.width), 'center_y': 1 - (5)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(button)
        
        button = Button(
            text=f'OFF', 
            size_hint=(None, None), 
            size=(button_width/2, button_height), 
            background_color=(1, 0, 0, 1), 
            pos_hint={'center_x': 0.5 + (button_width/4/Window.width), 'center_y': 1 - (5)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(button)
        
        button = Button(
            text=f'POWRÓT', 
            size_hint=(None, None), 
            size=(button_width, button_height), 
            background_color=(1, 0, 0, 1), 
            pos_hint={'center_x': 0.5, 'center_y': 1 - (6)*((button_height + button_spacing) / Window.height)}
        )
        button.bind(on_press=self.switch_to_main_page)
        layout.add_widget(button)
        
        self.res_label = Label(
            text="res", 
            font_size = button_height/3,
            size_hint=(None, None), 
            size=(button_width, button_height), 
            color = "ff0000",
            pos_hint={'center_x': 0.5, 'center_y': 1 - (7)*((button_height + button_spacing) / Window.height)}
        )
        layout.add_widget(self.res_label)
        
        
        self.add_widget(layout)
        
    def switch_to_main_page(self, instance):
        self.parent.current = 'main'

    def req_forserelayto_on(self, instance):
        try:
            res = requests.get(f"{SERVER}/forserelayto?power=on&time={self.input_box1}{self.input_box2}", timeout=2.5).status_code
            res = requests.get(f"{SERVER}/date", timeout=2.5).status_code
        except:
            res = "Błąd połączenia z mikrokontrolerem."
        self.res_label.text = str(res)

    