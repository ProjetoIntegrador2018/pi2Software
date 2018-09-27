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
    
    def change_db_cursor(self, *args):
        if int(args[1]) < 0:
            self.ids.barra_db.cursor_image = 'assets/cursor_amarelo.png'
        elif(args[1]) > 0:
            self.ids.barra_db.cursor_image = 'assets/cursor_vermelho.png'
        else:
            self.ids.barra_db.cursor_image = 'assets/cursor_verde.png'

        
class Menu(Screen):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
