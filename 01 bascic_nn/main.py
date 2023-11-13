import tensorflow as tf # importamos libreria TensorFlow
import numpy as np      # importamos numpy para ordenar arreglos facilmente 

# Datos de entrenamiento
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, -14, 32, 46, 59, 72, 100], dtype=float)

# capa simple
    # 
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([capa])

