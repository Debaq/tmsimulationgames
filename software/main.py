# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#                  NOMBRE PROYECTO : tmsimulation               #
#                   VER. 20.7.31 - GUI Kivy                     #
#                    NOMBRE VER. : TSG                          #
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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.properties import *

from kivy.config import Config
from kivy.clock import Clock

import requests

Config.set('graphics', 'width', '732')
Config.set('graphics', 'height', '412')
Config.set('graphics', 'resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')



loginTSG = False


class Btn (Button):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = None, None


class Login (BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       

    
class TitleWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MenuWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CenterWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.login = Login()
        button = Btn(text="ingresar", size_hint=(1,1), height=20,on_release=self.removePages)
        self.removePages()
        #button.bind(on_release=self.loginMeth)
        self.login.add_widget(button)
        
        self.add_widget(BoxLayout())
        self.add_widget(self.login)
        self.add_widget(BoxLayout())

    def removePages(self, *ignore):
        self.remove_widget(self.login)

    def loginMeth(self):
        global loginTSG
        user = self.login.ids.userInput.text
        passw = self.login.ids.passwordInput.text
        user.replace(" ", "")
        passw.replace(" ", "")
        loginTSG = True


class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        titleWidget = TitleWidget()
        centerWidget = CenterWidget()
        menuWidget = MenuWidget()
        self.add_widget(titleWidget)
        self.add_widget(centerWidget)
        self.add_widget(menuWidget)
        if loginTSG:
            print("entre a interfaces")
        

class tmsimulationApp(App):
    def build(self):
        #Clock.schedule_interval(self.update, 1)
        #self.update()
        return Interface()        

    def update(self, *args):
        self.root_widget = Interface()
        print(loginTSG)
        return self.root_widget

         
#################################################################
#                                                               #
#                  CONECTOR A LA API DE TMEDUCA                 #
#                                                               #
#################################################################



""" 
El siguiente código es para conectarse a la API de Fullaxis
Posee funciones:
     - para obtener las key del servicio de almacenaje
     - para enviar documentos al almacenaje
     - para recuperar docuemtnos del almacenaje 
     
Lógica de funcionamiento:

==================Interfaz====================
|  ▼ usuario y        ◘                   ▲ |
|  ▼ contraseña       ◘  entrega archivos ▲ |
|  ▼ .                ◘  al workspace     ▲ |
|==============API_CONECTOR.py=================
|  ▼ requests         ◘                   ▲ |
|  ▼ Server           ◘  conecta el  srv  ▲ |
|  ▼ .                ◘  al workspace     ▲ |
|  ▼ .                ◘  mediante las keys▲ |
|=================API.php=======================
|  ▼ verifica         ◘                   ▲ |
|  ▼ usuario y        ◘  entrega keys     ▲ |
|  ▼ contraseña       ◘  del server de    ▲ |
|  ▼ .                ◘  almacenaje       ▲ |
===================MYSQL=======================


    ejemplo:
        import API_conector
        Nombre = 'name'
        Password = 'pass123'
        data_conection = API_conector.request_key(Nombre, Password)
        app_key_id = data_conection[0]
        app_key = data_conection[1]
        bucket_name = data_conection[2]
        conection_b2 = API_conector.b2_conect(app_key_id, app_key, bucket_name)
"""

import requests
from b2sdk.v1 import *

## URL donde esta alojada la API
url = 'https://tmeduca.cl/TSG/lib/API.php'


def request_key(name_user, password):
    """request_key

    Args:
        name_user (str): Usuario
        password (str): Contraseña

    Returns:
        Lista: lista con [0]app_key_id, [1]app_key, [2]bucket_name
    """
    request_array = {'user':name_user, 'password': password} 
    response = requests.post(url, data=request_array)
    string_response=(response.text)
    string_response=string_response.split(',')
    return string_response
    
       
class b2_conect():
    """
    Para que funcione es necesario correr request_key(), con un usuario y pasword validos
    
    b2 conect permite conectarse al bucket especificado en la base de datos
    - listar los archivos existentes
    - descargar los archivos
    - cargar nuevos archivos
    
    """
    def __init__(self,app_key_id, app_key, app_bucket):
        """conección

        Args:
            app_key_id (str): id obtenido desde la base de datos generado por b2
            app_key ([type]): key obtenida desde la base de datos generado por b2
            app_bucket ([type]): bucket obtenido desde la base de datos generado por b2
        """
        self.info = InMemoryAccountInfo()
        self.b2_api = B2Api(self.info)
        application_key_id = app_key_id
        application_key = app_key
        self.app_bucket_name = app_bucket
        self.b2_api.authorize_account("production", application_key_id, application_key)
        
    
    def request_list(self):
        """request_list

        Returns:
            array: devuelve los archivos en un array, cada elemento posee [0]nombre,[1]timestamp,[2]carpeta
        """
        bucket = self.b2_api.get_bucket_by_name(self.app_bucket_name)
        result = []
        for file_info, folder_name in bucket.ls(show_versions=False):
            info = [file_info.file_name, file_info.upload_timestamp, folder_name]
            result.append(info)
        return result

    def upload_file(self, local_file_path, b2_file_name, file_info):

        bucket = self.b2_api.get_bucket_by_name(self.app_bucket_name)
        bucket.upload_local_file(
            local_file=local_file_path,
            file_name=b2_file_name,
            file_infos=file_info
        )

if __name__ == '__main__':
    tmsimulationApp().run()