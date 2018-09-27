from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from process_note import ToneLayout
import time

class Gerenciador(BoxLayout):
    pass

class TelaInicial(Screen):
    pass
    
class TelaAfinacao(Screen):
    pass

class Menu(Screen):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
