
# Contruccion red neuronal simple con TF


import tensorflow as tf # 
import numpy as np      # importamos numpy para ordenar arreglos facilmente 

# Datos de entrenamiento
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, -14, 32, 46, 59, 72, 100], dtype=float)

# capa simple
    # 
capa = tf.keras.layers.Dense(units=1, input_shape=[1])

'''
units: Este parámetro especifica el número de neuronas (o unidades) en la capa. 
En este caso, estás creando una capa con 1 unidad. 
Cada unidad en esta capa está conectada a todas las unidades en la capa anterior o de entrada (según el tipo de capa).

input_shape: Este parámetro se utiliza para definir la forma de los datos de entrada que se esperan en esta capa. 
En este caso, input_shape se establece en [1], lo que significa que la capa espera datos de entrada unidimensionales 
(vectores) con una sola característica. 
Por ejemplo, si estás diseñando una red neuronal para resolver un problema de regresión simple en el que tienes una sola característica de entrada, 
como predecir el precio de una casa basado en su área, establecerías input_shape en [1] para indicar que la capa espera un solo valor numérico como entrada.
'''

model = tf.keras.Sequential([capa])

