# Programa 2.7 
El bar
# Explicación del programa.

Solicita al usuario que ingrese su edad y la convierte a un número entero (int).
```python
edad = int(input("Ingresa tu edad: ")) 
```

Condición IF: Si la edad es mayor o igual a 18
```python
if edad >= 18:
```
 ``print("Puede ingresar al bar")``  Si la edad es mayor o igual a 18, se imprime este mensaje.
 
 Condición ELSE: Si la edad es menor a 18
 ```python
 else:
```
  ``print("Vete a tu casa niñ@ rataaaa")``   Si la edad es menor que 18, se imprime este mensaje.

``print("\n")``   Salto de línea para separar el resultado de la siguiente salida.

``print("fin del programa")``   Imprime "fin del programa" para indicar que el programa ha terminado.


## Explicación de cada parte:
```python
edad = int(input("Ingresa tu edad: ")):
```
``input()``: Solicita al usuario que ingrese un valor. Por defecto, el valor ingresado es tratado como una cadena de texto (string).

``int()``: Convierte el valor ingresado a un número entero. Esto es necesario porque vamos a comparar la edad (un número) con 18.

Condicional ``if``:

``if edad >= 18:``: Si la edad es mayor o igual a 18, ejecutará el bloque de código dentro de esa condición (en este caso, imprimir el mensaje "Puede ingresar al bar").

``else:``: Si la condición del ``if`` no se cumple (es decir, si la edad es menor que 18), se ejecutará el bloque dentro del ``else`` (en este caso, imprimir el mensaje "Vete a tu casa niñ@ rataaaa")
