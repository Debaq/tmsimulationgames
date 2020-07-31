# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#                  NOMBRE PROYECTO : tmsimulation               #
#                   VER. 20.7.31 - GUI Kivy                     #
#                    NOMBRE VER. : XXX                          #
#        DESAROLLADORES : NICOLÁS QUEZADA QUEZADA               #
#                       : CRISTIAN LEIVA FERNÁNDEZ              #
#                                                               #
#################################################################

# ==> LIBRERIAS BÁSICAS

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button




class MenuBar(BoxLayout):
     pass




# Boxlayout is the App class
class tmsimulation(App):
    def build(self):
        #superBox        = BoxLayout(orientation='vertical')
        
        #horizontalBox   = BoxLayout(orientation='horizontal')
        #button1         = Button(text="One")
        #button2         = Button(text="Two")
        #horizontalBox.add_widget(button1)
        #horizontalBox.add_widget(button2)
        #verticalBox     = BoxLayout(orientation='vertical')
        #button3         = Button(text="Three")
        #button4         = Button(text="Four")
        #verticalBox.add_widget(button3)
        #verticalBox.add_widget(button4)
        #superBox.add_widget(horizontalBox)
        #superBox.add_widget(verticalBox)
        return MenuBar()

   

 

# Instantiate and run the kivy app

if __name__ == '__main__':
    tmsimulation().run()
