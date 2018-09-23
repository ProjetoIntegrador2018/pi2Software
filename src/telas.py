from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

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
