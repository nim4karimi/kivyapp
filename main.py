'''
Application to callculate - Herotek.ir
==========================================

***INPUTS***
--> 1 | ertefa
--> 2 | arz
--> 3 | gheymat

------------------
***OUTPUTS***
--> 1 | ertefa_frame    ==> ertefa - 6
--> 2 | arz_frame       ==> arz - 6
--> 3 | motaharek       ==> ertefa - 7.5

--> 4 | ertefa_tor      ==> ertefa - 3.5
--> 5 | gam_tor         ==> arz / 2.5

--> 6 | metr_moraba     ==> ertefa X arz
--> 7 | gheymat_koll    ==> metr_moraba X gheymat
'''

import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


import arabic_reshaper
from bidi.algorithm import get_display

# ---------------------------------------------------
# Reshape Texts
# *** Inputs Text
ertefa_text = arabic_reshaper.reshape(u'ارتفاع اصلی')
reshape_ertefa_text = get_display(ertefa_text)

arz_text = arabic_reshaper.reshape(u'عرض اصلی')
reshape_arz_text = get_display(arz_text)

gheymat_text = arabic_reshaper.reshape(u'قیمت واحد')
reshape_gheymat_text = get_display(gheymat_text)

# =================
# *** Outputs text
ertefa_frame_text= 'ارتفاع فریم'
arz_frame_text = 'عرض فریم'
motaharek = 'متحرک'
# -- section 2
ertefa_tor_text = 'ارتفاع تور'
gam_tor_text = 'گام تور'
# -- section3
metr_moraba_text = 'متر مربع'
gheymat_koll_text = 'قیمت کل'
# ---------------------------------------------------


class Hero(App):

    def build(self):
        self.icon = 'icon.png'
        self.title = 'ملزومات توری های پلیسه تورسان'
        # Main Layout
        w = BoxLayout(orientation='vertical')
        label1 = Label(text = reshape_ertefa_text , font_name='yekan.ttf' , font_size = 18)
        label2 = Label(text = reshape_arz_text , font_name='yekan.ttf' , font_size = 18)
        w.add_widget(label1)
        w.add_widget(label2)

        # return a Button() as a root widget
        return w




if __name__ == '__main__':
    Hero().run()