# Programa 3_3
Identificación de tipos de datos en Python
# Explicación del programa


Solicitamos al usuario que ingrese su edad. La función `input()` devuelve un valor de tipo `str`, que es una cadena de texto. Por lo tanto, la variable `variable` se almacena inicialmente como una cadena de caracteres.
```python
variable = input("Ingresa tu edad:")
print(type(variable))
```

En este paso, convertimos el valor de la variable `variable` de tipo `str` (cadena de texto) a tipo `int` (entero). La función `int()` permite hacer esta conversión para tratar la edad como un número entero.
```python
variable = int(variable)
print(type(variable))
```

Por último, convertimos la variable `variable` de tipo `int` (entero) a tipo `float` (número decimal). Esto se logra usando la función `float()`, lo que permite tratar la variable como un número de punto flotante.
```python
variable = float(variable)
print(type(variable))
```
