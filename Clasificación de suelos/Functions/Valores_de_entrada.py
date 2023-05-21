# Librerias
import pandas as pd
import numpy as np

# Data frame con los datos obtenidos al realizar el ensayo de granulometría
granulometria = pd.DataFrame(
    {
        "Tamiz": pd.Categorical(["N°4", "N°10", "N°20", "N°40", "N°60", "N°140", "N°200", "Fondo"]), #Columna con los nombres de los tamices
        "Abertura": [4.75, 2, 0.85, 0.425, 0.25, 0.106, 0.075, np.nan], #Columna con los tamaños de las aberturas de los tamices en mm
        "Masa_retenida":[205.3, 240.6, 179.1, 87.5, 64.9, 50.9, 9.8, 50] #Columna con las masas retenidas en los tamices
    }
)   

# Suma de las masas retenidas en los tamices, es decir el peso total de la muestra ensayada
Masa_total = granulometria["Masa_retenida"].sum()
print(Masa_total)

# Data frame con las operaciones que se deben realizar
granulometria["Retenido"]=round(granulometria["Masa_retenida"]/Masa_total*100,1) #Porcentaje que representa la masa retenida en el tamiz sobre la masa total de la muestra
granulometria["Retenido_acumulado"]=round(granulometria["Retenido"].cumsum(),1) #Suma acumulada de los porcentajes retenidos
granulometria["Pasa"]=round(granulometria["Retenido_acumulado"].values[7]-granulometria["Retenido_acumulado"],1) #Porcentaje final retenido acumulado menos cada uno de los porcentajes retenidos acumulados
print(granulometria)
    
# Pasa 4
Pasa_4 = granulometria.at[0, 'Pasa']

# Pasa 200
Pasa_200 = granulometria.at[6, 'Pasa']

#Limite liquido
LL = 60

# Indice de plasticidad
IP = 20