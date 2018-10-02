import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.clock import Clock


class Gerenciador(BoxLayout):
    pass

class TelaInicial(Screen):
    pass
    
class TelaAfinacao(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    
    def show_db(self, *args):
        self.ids.decibeis.text = str(int(args[1])) + ' decibéis'
    
    def change_db_cursor(self, *args):
        if int(args[1]) < 0:
            self.ids.barra_db.cursor_image = 'assets/cursor_amarelo.png'
        elif(args[1]) > 0:
            self.ids.barra_db.cursor_image = 'assets/cursor_vermelho.png'
        else:
            self.ids.barra_db.cursor_image = 'assets/cursor_verde.png'
    
    def mock_db_value(self):
        while True:
            self.ids.barra_db.value = random.randint(-50, 50)
            return self.ids.barra_db.value
    
    def disable_touch_event(self):
        return 0
        
    def update(self, *args):
        self.ids.barra_db.value = self.mock_db_value()
        
        
        
class Menu(Screen):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
