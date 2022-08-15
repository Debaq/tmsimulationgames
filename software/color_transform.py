# -*- coding: utf-8 -*-

#################################################################
#                                                               #
#          NOMBRE PROYECTO : tmsimulation                       #
#          LIBRERIA : RGB_TO_PERCENT                            #
#          VER. 1 - CLI                                         #
#          NOMBRE VER. : RGB to PERCENT                         #
#          DESAROLLADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################


def rgb_Per(R,G,B,A=255):
    """rbg_Per: transforma los codigos rgba a porcentaje
                puede utilizarce rgb u rgba, se devuelve 
                str en porcentaje del 0 al 1

    Args:
        R (int): Color Rojo 0 - 255
        G (int): Color Verde 0 - 255
        B (int): Color Azul 0 - 255
        A (int, optional): Alpha 0 - 255. Defaults to 255.
    """
    rgba = [R,G,B,A]
    out=[]
    for a in rgba:
        result = (a/255)
        out.append(result)

    return (str(out).strip('[]'))
    
    

if __name__ == "__main__":
    print(rgb_Per(136,14,79))