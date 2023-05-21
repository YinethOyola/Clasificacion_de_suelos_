import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
from .Valores_de_entrada import *
from .Carta_de_plasticidad import *
from .Granulometria import *

def Clasificacion():
# Condicionales
    if Pasa_200 > 50: # Finos  
        Carta_de_plasticidad(LL,IP)
    else: # Gruesos
        if Pasa_4 > 50: # Arenas
            if Pasa_200 < 5:
                if Cu > 6 and Cc < 3:
                    print("El suelo esta clasificado como SW - arena bien gradada")
                else:
                    print("El suelo esta clasificado como SP - arena mal gradada")
            elif 5 < Pasa_200 < 12:
                if Cu > 6 and Cc < 3:
                    print("El suelo esta clasificado como SW - arena bien gradada")
                    Carta_de_plasticidad(LL,IP)
                else:
                    print("El suelo esta clasificado como SP - arena mal gradada")
                    Carta_de_plasticidad(LL,IP)
            else:
                Carta_de_plasticidad(LL,IP)
        else: # Gravas
            if Pasa_200 < 5:
                if Cu > 6 and Cc < 3:
                    print("El suelo esta clasificado como GW - grava bien gradada")
                else:
                    print("El suelo esta clasificado como GP - grava mal gradada")
            elif 5 < Pasa_200 < 12:
                if Cu > 6 and Cc < 3:
                    print("El suelo esta clasificado como GW - grava bien gradada")
                    Carta_de_plasticidad(LL,IP)
                else:
                    print("El suelo esta clasificado como GP - grava mal gradada")
                    Carta_de_plasticidad(LL,IP)
            else:
                Carta_de_plasticidad(LL,IP) 

