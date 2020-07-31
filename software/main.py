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

# ==> Titulo de la ventana y Versión
def titleVer():
    """Titulo y versión
    Returns:
        str: titulo y versión del programa
    """
    title = "TSG"
    ver = 0.1
    out = title+" "+str(ver)
    return out


# ==> LIBRERIAS BÁSICAS
import kivy
kivy.require('1.11.0')
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from color_transform import rgb_Per
from kivy.config import Config

Config.set('graphics', 'width', '732')
Config.set('graphics', 'height', '412')
Config.set('graphics', 'resizable', False)

class RootWidget(BoxLayout):
    """Widget Principal
    """
    def __init__(self, **kwargs):
        # Todas las funcionalidades agregadas al Widget
        super(RootWidget, self).__init__(**kwargs)

        # se agregan los widgets principales

class MenuBar(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        self.title=titleVer()
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(1,1,1,1)  # Color predeterminado de fondo (Blanco)
            self.rect = Rectangle(size=root.size, pos=root.pos) #Se agrega el color blanco en el fondo
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()