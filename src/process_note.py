from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.core.text import LabelBase
from math import log2, pow                                                                                                         
import time
import random
from functools import partial


LabelBase.register(name='DigitalFont',fn_regular="../font/digital-readout.heavy-oblique.ttf")

class ToneLayout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update,1/1.)

        self.musical_note = NoteLabel(text='---',
                               size_hint=(1, 2.5),
                               color=(0,1,0,1),
                               font_size=300,
                               font_name='DigitalFont')

        self.octave = NoteLabel(text='---', 
                        size_hint=(1.40, 2),
                        font_size=100,
                        color=(0,1,0,1),
                        font_name='DigitalFont')
        
        self.add_widget(self.musical_note)
        self.add_widget(self.octave)

    def update(self,*args):
        name,octave = mock_randon_data()
        self.musical_note.setText(str(name))
        self.octave.text = octave 


class NoteLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #Clock.schedule_interval(self.update,50)
        self.aux_text = ''

    def setText(self, text):
        self.text = text

    def update(self,*args):
        self.text = ''


#This function is just for mocking purpose
def mock_randon_data():
    rand_freq = random.randint(0,100)
    A4 = 440                                                                                                                           
    C0 = A4*pow(2, -4.75)  
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]         
    try:                                                                                                                                                                    
        h = round(12*log2(rand_freq/C0))                                                                                                
        octave = h // 12                                                                                                           
        n = h % 12
        return (name[n],str(octave))
    except ValueError:
        return ('---', '') 


