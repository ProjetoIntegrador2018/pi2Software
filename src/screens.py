import time
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
import time
import store
from kivy.lang import Builder


Builder.load_file('kv/application.kv')


class Manager(BoxLayout):
    pass


class HomeScreen(Screen):
    background_color = ListProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Clock.schedule_interval(self.battery_level, 1)
        #Clock.schedule_interval(self.battery_level_icons, 1)

    def battery_level(self, *args):
        #proc = os.popen("./battery.sh")
        #level = proc.readlines()
        #level = str(level)
        #level = level.replace("[", "")
        #level = level.replace("]", "")
        #level = level.replace("'", "")
        #level = level.replace("n", "")
        #level = level[0:-1]
        self.ids.battery.text = str('100% ')
        return self.ids.battery.text

    def battery_level_icons(self, *args):
        val = self.ids.battery.text.replace("%", "")
        if int(val) > 80:
            self.ids.icon_battery.source = 'assets/img/battery_100.png'
        elif int(val) >= 60 and int(val) <= 79:
            self.ids.icon_battery.source = 'assets/img/battery_70.png'
        elif int(val) >= 40 and int(val) <= 59:
            self.ids.icon_battery.source = 'assets/img/battery_50.png'
        elif int(val) >= 20 and int(val) <= 39:
            self.ids.icon_battery.source = 'assets/img/battery_20.png'
        elif int(val) >= 0 and int(val) <= 19:
            self.ids.icon_battery.source = 'assets/img/battery_0.png'
        else:
            pass

    def set_hold_tight(self):
        store.hold_tight = True

    def set_loosen(self):
        store.loosen = True

    def go_tunner(self):
        store.cancel = False
        self.manager.current = "tuningScreen"


class TuningScreen(Screen):
    background_color = ListProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.max_iteration = 100 
        Clock.schedule_interval(self.update, 1/10)
        Clock.schedule_interval(self.update_progress_bar, 1/10)

        self.popup = None
        self.cord = 0
        self.timestep = 0

    def confirm_return(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(
            Label(
                text="Tem certeza que deseja voltar?\n Isso cancelará seu progresso"
            )
        )
        btn1 = Button(text="Sim")
        btn2 = Button(text="Cancelar")
        box.add_widget(btn1)
        box.add_widget(btn2)

        self.popup = Popup(title='Tem certeza que deseja fazer isso ?',
                           title_size=(30),
                           title_align='center', content=box,
                           size_hint=(None, None), size=(400, 400),
                           auto_dismiss=True)

        btn1.bind(on_press=lambda x: self.goToInit())
        btn2.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def goToInit(self):
        self.cord = 0
        self.ids.progress_bar.value = 0
        self.popup.dismiss()
        self.manager.current = "homeScreen"

    def show_tuning_data(self, *args):
        if(self.cord<6):
            aux_cord = self.cord+1
        else:
            aux_cord = self.cord
        
        self.ids.frequency.text = str(
            store.frequency) + ' Hz'+'         Corda: ' + str(aux_cord)

    def change_db_cursor(self, *args):
        if int(args[1]) < 0:
            self.ids.db_bar.cursor_image = 'assets/img/cursor_yellow.png'
        elif(args[1]) > 0:
            self.ids.db_bar.cursor_image = 'assets/img/cursor_red.png'
        else:
            self.ids.db_bar.cursor_image = 'assets/img/cursor_green.png'

    def frequency_range(self):
        cord_values = [329, 246, 196, 146, 110, 82, 404]
        self.ids.db_bar.value = abs(int(store.frequency) - cord_values[self.cord])
        if(self.timestep < time.time()):
            if(self.ids.db_bar.value <= 5  and self.cord != 6):
                self.cord = (self.cord + 1)
            self.timestep = time.time() + 1
        return self.ids.db_bar.value

    def disable_touch_event(self):
        return 0

    def update(self, *args):
        self.ids.db_bar.value = self.frequency_range()

    def show_progress_bar(self, *args):
        self.ids.progress.text = str(
            int(self.ids.progress_bar.value)) + '% afinado'

    def update_progress_bar(self, *args):
        if self.ids.progress_bar.value >= 100:
            self.ids.progress.text = 'Afinado!'
            return False
        self.ids.progress_bar.value = self.cord * 16.7


class Menu(Screen):
    light_theme = True
    dark_theme = False

    def rasp_shutdown(self, *args):
        os.system('sudo shutdown now')

    def change_theme(self):
        if self.light_theme:
            self.ids.theme_icon.source = 'assets/img/light_bulb_icon_grey.png'
            self.parent.ids.logo_icon.source = 'assets/img/guitar_icon_grey.png'
            self.ids.shutdown_icon.source = 'assets/img/shutdown_icon_grey.png'

            # Dark gray
            self.parent.background_color = utils.get_color_from_hex('#404040')

            self.light_theme = False
            self.dark_theme = True
        elif self.dark_theme:
            self.ids.theme_icon.source = 'assets/img/light_bulb_icon_black.png'
            self.ids.shutdown_icon.source = 'assets/img/shutdown_icon_black.png'
            self.parent.ids.logo_icon.source = 'assets/img/guitar_icon_black.png'

            # Light gray
            self.parent.background_color = utils.get_color_from_hex('#E0E0E0')

            self.light_theme = True
            self.dark_theme = False


class MenuButton(Button):
    pass


class Application(App):
    def build(self):
        return Manager()
