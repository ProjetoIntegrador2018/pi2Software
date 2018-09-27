from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.graphics import Color
from process_note import ToneLayout
import time

class Gerenciador(BoxLayout):
    pass

class TelaInicial(Screen):
    pass
    
class TelaAfinacao(Screen):
    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.popup = None

    def confirm_return(self):
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(Label(text = "Tem certeza que deseja voltar?\n Isso cancelara seu progresso"))
        btn1 = Button(text = "Sim")
        btn2 = Button(text = "Cancelar")
        box.add_widget(btn1)
        box.add_widget(btn2)

        self.popup = Popup(title='Tem certeza que deseja fazer isso ?', title_size= (30), 
                  title_align = 'center', content = box,
                  size_hint=(None, None), size=(400, 400),
                  auto_dismiss = True)

        btn1.bind(on_press = lambda x: self.goToInit())
        btn2.bind(on_press = self.popup.dismiss)
        self.popup.open()

    def goToInit(self):
        self.popup.dismiss()
        self.manager.current = "telaInicial"
        
class Menu(Screen):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
