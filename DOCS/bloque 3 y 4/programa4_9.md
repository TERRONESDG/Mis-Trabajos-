# programa 4_9
Deducir si un número es primo entre el 10 y 90.
# Explicación del programa

### Verificar el rango del número:
```python
if 10 <= numero <= 90:
```
Este condicional asegura que el número ingresado esté dentro del rango especificado (10 a 90). Si no lo está, se muestra un mensaje de error.

### Variable es_primo:
```python
es_primo = True
```
Inicialmente, asumimos que el número es primo. Si encontramos algún divisor distinto de 1 y del propio número, cambiamos esta variable a False.

### Bucle para verificar divisores:
```python
for i in range(2, int(math.sqrt(numero)) + 1):  
    if numero % i == 0:
        es_primo = False
        break
```
## Tabla de iteración 
| Iteración | i   | número % i | ¿Es divisible? | ¿Es primo? |
|-----------|-----|------------|----------------|------------|
|     1     |  2  |     1      |      No        |   True     |
|     2     |  3  |     1      |      No        |   True     |
|     3     |  4  |     1      |      No        |   True     |
|     4     |  5  |     4      |      No        |   True     |
|     5     |  6  |     1      |      No        |   True     |
|     6     |  7  |     0      |      Sí        |   False    |

El bucle verifica si el número es divisible por cualquier número entre 2 y la raíz cuadrada del número.
Si se encuentra un divisor, el número no es primo y el bucle termina con break.

### Mostrar el resultado:
``` python
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
````
Dependiendo del valor de es_primo, se muestra el mensaje correspondiente.

### Control de errores: 
Si el número ingresado no está en el rango (10-90), se muestra un mensaje indicando que el valor no es válido:
```python
else:
    print("Por favor, ingrese un número entre 10 y 90.")
````
## Ejemplo de Ejecución
### Entrada:
```` python
Ingrese un número entre 10 y 90: 37
````
### Salida:
```python
37 es un número primo.
````
### Entrada fuera de rango:
```python
Ingrese un número entre 10 y 90: 100
```
### Salida:
```python
Por favor, ingrese un número entre 10 y 90.
````
