# Machine Learning Fundamentals A - TensorFlow 2.0 Course

## Inteligencia artificial
Pueden pensar las computadoras?
Podemos hacer que descubran las cosas?
Alejarnos de la codificacion estricta

### Definicion de IA
Simplmenete un algoritmo que imita un comportamiento humano intelectual, desde algo muy simple como seguir un conjunto de reglas, hasta algo muy complejo como predecir o intuir un valor.

### Apredizage automatico (Machine learning (ML))
Modelos que infieren las reglas con base auna serie de datos entregado, es decir por medio de una serie de datos ejemplo, el modelo creara una serie de reglas con base a los datos dados creando un modelo matematico que explique el comportamiento de los datos de ejemplo, de esta forma el modelo podra generar una respuesta con base a estas reglas inferidas. 

### Apremdizage prodfundo (Aprendizage profundo) / Redes Nauronales (NN)

### Que es un Tensor
Son matrices de n dimensiones de tipos de datos base, un tensor es un calculo previamente definido que enventualmente producira un valor, los tipos de datos pueden ser numericos, cadenas, flotantes.

#### Importando TF
```
import tensorflow as tf
print(tf.version)
```

#### Ejemplo de declaracion de variables
```
string = tf.Variable("string input", tf.string)
number = tf.Variable(324, tf.int16)
float = tf.Variable(3.567, tf.float64)
```


#### Variables dimensionales
Tensor de grado uno / es solamente una lista de datos de una sola dimension
```
rank_tensor_1 = tf.Variable(["Test", "ok", "Tim"], tf.string)
```
Tensor de grado dos / dos listas /  dos dimensiones
```
rank_tensor_2 = tf.Variable([["Test", "ok"], ["Test", "yes"]], tf.string)
```
#### Determinar el rango de un Tensor
```
tf.rank(rank_tensor_2)
2 -> dos dimensiones 
```
#### Determinar el numero de elementos en cada rango
```
rank_tensor_2.shape
[2, 2] -> dos elementos, cada elemento tiene 2 datos
```
#### Generadores de Tensores
tf.ones([1, 2, 3]) crea un tensor tridimensional con forma [1, 2, 3], lo que significa que tiene una dimensión exterior de tamaño 1, una dimensión intermedia de tamaño 2 y una dimensión interior de tamaño 3. 
```
tensor1 = tf.ones([1,2,3]) 
#tf.ones() es una función en TensorFlow para crear tensores llenos de unos
#tf.zeros() es una función en TensorFlow para crear tensores llenos de ceros
print(tensor1)
tf.Tensor([[[1. 1. 1.]
  [1. 1. 1.]]], shape=(1, 2, 3), dtype=float32)
```

#### Reordenar Tensores
La función tf.reshape en TensorFlow se utiliza para cambiar la forma de un tensor sin cambiar sus valores. Puedes ajustar las dimensiones del tensor según tus necesidades.

```
tensor2 = tf.reshape(tensor1, [2,3, 1])
print(tensor2)
tf.Tensor([[[1.]
  [1.]
  [1.]]

 [[1.]
  [1.]
  [1.]]], shape=(1, 2, 3), dtype=float32)
```
Lo que ha sucedido aquí es que has cambiado la forma de tensor1 de [1, 2, 3] a [2, 3, 1]. Ahora, el tensor tiene una dimensión exterior de tamaño 2, una dimensión intermedia de tamaño 3 y una dimensión interior de tamaño 1. 
#### Tipos de tensores
* Variables # pueden cambiar el valor una vez creado el tensor
* Constant  # los valores del tensor son inmutables una vez creado
* Placeholder
* SparseTensor

#### Evaluando tensores
Para evaluar un tensor es necesario crear una sesion esto en version 1 para version 2 ya no es necesario, desde el punto de vista e codigo es necesario evaluar un tensro cuando se quieren obtener valores concretos del tensor, esto es útil para inspeccionar o imprimir los resultados de operaciones, otro caso es hacer un debugging para encontrar errores y entender el flujo de datos a través de tu modelo, entro otras cosas.
```
TensorFlow v1 --------------------------------------------------
with tf.Session() as sess:
    tensor.eval()

TensorFlow v2 --------------------------------------------------
# Crear un tensor
tensor = tf.constant([1, 2, 3])

# Evaluar el tensor para obtener los valores concretos
result = tensor.numpy()
```
