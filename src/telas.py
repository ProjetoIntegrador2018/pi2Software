import random
import os

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
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty, ListProperty, StringProperty
import kivy.utils as utils


class Gerenciador(BoxLayout):
    pass

class TelaInicial(Screen):
    my_color = ListProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.battery_level, 1)
   
    def battery_level(self, *args):
        proc = os.popen("acpi")
        level = proc.readlines()
        level = str(level)
        level = level.replace(",", "")
        level = level.replace("]", "")            
        level = level.replace("'", "")
        level = level.replace("n", "")
        level = level[0:-1]
        level = level.replace("", "")
        level = level.split(" ")
        self.ids.battery.text = str("Battery "+level[3])
        return self.ids.battery.text

	
class TelaAfinacao(Screen):

    my_color = ListProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
        Clock.schedule_interval(self.update_progress_bar, 1/10)
        
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


        
    def show_progress_bar(self, *args):
        self.ids.progress.text = str(int(self.ids.progress_bar.value)) + '% afinado'

    def update_progress_bar(self, *args):
        if self.ids.progress_bar.value >= 100:
            self.ids.progress.text = 'Afinado!'
            return False
        self.ids.progress_bar.value += 1
        
           
class Menu(Screen):
    light_theme = True
    dark_theme = False

    def rasp_shutdown(self, *args):
        os.system('sudo shutdown now')

    def change_theme(self):
        if self.light_theme:
            self.ids.theme_icon.source = 'assets/light_bulb_icon_grey.png'
            self.parent.ids.logo_icon.source = 'assets/guitar_icon_grey.png'
            self.ids.shutdown_icon.source = 'assets/shutdown_icon_grey.png'
            
            # Cinza escuro
            self.parent.my_color = utils.get_color_from_hex('#404040')
            
            self.light_theme = False
            self.dark_theme = True
        elif self.dark_theme:
            self.ids.theme_icon.source = 'assets/light_bulb_icon_black.png'
            self.ids.shutdown_icon.source = 'assets/shutdown_icon_black.png'
            self.parent.ids.logo_icon.source = 'assets/guitar_icon_black.png'
            
            # Cinza claro
            self.parent.my_color = utils.get_color_from_hex('#E0E0E0')
            
            self.light_theme = True
            self.dark_theme = False

class MenuButton(Button):
    pass

class Aplicacao(App):
    def build(self):
        return Gerenciador()
