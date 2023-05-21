#Importar librerias a utilizar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from .Valores_de_entrada import *
    
# Se grafica la línea de la granulometría
plt.figure(figsize=(14, 4)) 
plt.plot(granulometria.Abertura, granulometria.Pasa, linestyle='-', marker='o', color='m', fillstyle='none',label='Data')
f = interp1d(granulometria.Pasa, granulometria.Abertura)

#Calcular D60 D50 D30 D10
#valores de entrada
y1_coord = 60
y2_coord = 30
y3_coord = 10
#Realiza interpolación
x1_coord = f(y1_coord)
x2_coord = f(y2_coord)
x3_coord = f(y3_coord)
#Solo toma dos decimales
x1_formatted = "{:.2f}".format(x1_coord)
x2_formatted = "{:.2f}".format(x2_coord)
x3_formatted = "{:.2f}".format(x3_coord)
#Los ubica en el plano
plt.scatter(x1_coord, y1_coord, marker="s", s=50, color="blue", label="D60="+x1_formatted)
plt.scatter(x2_coord, y2_coord, marker="<", s=50, color="green", label="D50="+x2_formatted)
plt.scatter(x3_coord, y3_coord, marker=">", s=50, color="brown", label="D30="+x3_formatted)

#Grafica
plt.title("Curva granulométrica", color="purple", size = 15, y = 1.4)
plt.xlabel("Diámetro (mm)")
plt.ylabel("Porcentaje pasa (%)")
plt.legend() 
plt.xscale("log")
plt.xlim(0.07,5)
plt.ylim(0,100) 
plt.grid(color="k",lw="0.1",ls="-")

#se agregan más grillas
ax1 = plt.gca()
ax1.invert_xaxis()

# Agregar el segundo eje x para los nombres de los tamices
ax2 = ax1.twiny()
ax2.set_xscale("log")
ax2.set_xticks(granulometria.Abertura)
ax2.set_xticklabels(granulometria.Tamiz, rotation=90, fontsize=8)

# Agregar linas de los tamices
ax2.set_xlabel("Tamices")
ax2.set_xlim(0.07,5)
ax2.invert_xaxis()

#agregamos nombre lineas verticales
L_No4 = ([4.75,4.75]) 
L_No10 = ([2,2]) 
L_No20 = ([0.850,0.850]) 
L_No40 = ([0.425,0.425]) 
L_No60 = ([0.250,0.250])
L_No140 = ([0.106,0.106])  
L_No200 = ([0.075,0.075]) 
L_rango = ([0,100])

#se indicca en el plot la ubicación de estas líneas
plt.plot(L_No4, L_rango, color="grey", lw="0.8", ls="--")
plt.plot(L_No10, L_rango, color="grey", lw="0.8", ls="--")
plt.plot(L_No20, L_rango, color="grey", lw="0.8", ls="--") 
plt.plot(L_No40, L_rango, color="grey", lw="0.8", ls="--")
plt.plot(L_No60, L_rango, color="grey", lw="0.8", ls="--")
plt.plot(L_No140, L_rango, color="grey", lw="0.8", ls="--")
plt.plot(L_No200, L_rango, color="grey", lw="0.8", ls="--")

#se agrega textos
plt.text(4.95, 5, "Grava(Fina)", fontsize=6, rotation=90)
plt.text(2.08, 5, "Arena(Gruesa)", fontsize=6, rotation=90)
plt.text(0.445, 5, "Arena(Mediana)", fontsize=6, rotation=90)
plt.text(0.078, 5, "Arena(Fina)", fontsize=6, rotation=90)

x_values = [4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08]
for x in x_values:
    plt.axvline(x=x, color="grey", ls="-", lw="0.3")

# Ajuste de la gráfica
plt.subplots_adjust(bottom = 0.13, top = 0.69) 

plt.show()

# D6O, D30 Y D10
D60 = x1_coord
D30 = x2_coord
D10 = x3_coord

# Cu y Cc
Cu = D60/D10
Cc = (D30**2)/(D10*D60)
        

