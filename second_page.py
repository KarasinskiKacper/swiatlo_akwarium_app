from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

class SecondPage(Screen):
    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)
        
        
        self.label = Label(text='Second Page', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.label)
