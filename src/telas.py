from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class Gerenciador(BoxLayout):
    pass

class TelaInicial(Screen):
    pass
    
class TelaAfinacao(Screen):
    
    def show_db(self, *args):
        self.ids.decibeis.text = str(int(args[1]))
    
    # Teste de comportamento
    def test(self, *args):
        if int(args[1]) == 50:
            self.ids.barra_db.value = 0
        
class Menu(Screen):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
