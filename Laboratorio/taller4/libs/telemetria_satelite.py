# Primero partire importando las librerias:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Ahora procederemos a generar los datos que estaran en el archivo csv.

np.random.seed(42)  # Genera datos aleatorios, en este caso la forma 42.
flechas = pd.date_range(start='2026-10-01', periods=200, freq='D') # Genera un rango de fechas y horas. 
df_sim = pd.DataFrame({
    'fecha': flechas, #Genera una columna de fechas.
    'voltaje_V': np.random.normal(12.0, 0.5, 200),  # Genera una columna de voltaje.
    'temperatura_C': np.random.normal(20.0, 0.5, 200),   # Esto genera una columna de temperatura.
    'estado_bateria': np.random.choice(['OK', 'Precausión', 'Crítico'], 200, p=[0.8, 0.15, 0.05]) #Genera una columna de estados de la bateria, que va des de OK, Precausión y Crítico.
})


# Inyectar ruido (Datos nulos / NaN) para que el estudiante los limpie

df_sim.loc[20:25, 'voltaje_V'] = np.nan  #Recordar de .loc nos sirve para seleccionar una columna.
df_sim.loc[150:160, 'temperatura_C'] = np.nan # Aqui tambien inyecta ruido en la columna de temperaturas.
df_sim.to_csv('telemetria_satelite.csv', index=False) # Esto genera un archivo csv con los datos generados


# 2. Generador de Imagen Sintética (NumPy) (Imagen 200x200 de 3 canales (RGB))

img_sim = np.zeros((400, 400, 3), dtype=np.uint8)
# Crear un gradiente simple en cada canal
for i in range(400): 
    img_sim[:, i, 0] = int(255 * (i / 400))      # Canal Rojo (aumenta hacia la derecha)
    img_sim[i, :, 1] = int(255 * (i / 400))      # Canal Verde (aumenta hacia abajo)
    img_sim[:, :, 2] = 128                       # Canal Azul (constante)

plt.imsave('captura_satelite.jpg', img_sim)
print("Archivos de prueba creados: 'telemetria_satelite.csv' y 'captura_satelite.jpg'")