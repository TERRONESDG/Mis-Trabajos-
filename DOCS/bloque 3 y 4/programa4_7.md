# programa 4_7

# Explicación del programa

### Definición de la función ``operaciones``:
```python
def operaciones(num1, num2, digitos):
```
La función ``operaciones`` realiza cinco operaciones básicas (suma, resta, multiplicación, división y módulo) sobre los dos números proporcionados (``num1`` y ``num2``) y muestra los resultados. La división se formatea para mostrar la cantidad de decimales especificada en ``digitos``.

### Solicitud de datos al usuario:
```python
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))
```
Se solicitan al usuario los números ``num1``, ``num2``, el número de decimales para mostrar en los resultados (``digitos``) y el número de iteraciones en las que se debe duplicar el valor de los números.

### Ciclo ``for`` para iterar y duplicar los números:

```python
for i in range(iteraciones):
    operaciones(num1, num2, digitos)
    num1 *= 2
    num2 *= 2
```
El ciclo ``for`` se ejecuta tantas veces como el número ingresado en ``iteraciones``.


En cada iteración, se llama a la función ``operaciones`` con los valores actuales de ``num1`` y ``num2``.

Luego, los valores de ``num1`` y ``num2`` se duplican (se multiplican por 2) para la siguiente iteración.
Ejemplo de Salida
## tabla de iteracion 

| Iteración | num1 | num2 | Suma  | Resta | Multiplicación | División | Módulo |
|-----------|------|------|-------|-------|-----------------|----------|--------|
|     1     |   3  |   5  |   8   |  -2   |       15        |   0.60   |    3   |
|     2     |   6  |  10  |  16   |  -4   |       60        |   0.60   |    6   |
|     3     |  12  |  20  |  32   |  -8   |      240        |   0.60   |   12   |


### Si el usuario ingresa los siguientes valores:
```python
Ingrese el primer número: 3
Ingrese el segundo número: 2
Ingrese la cantidad de decimales a mostrar en la división y módulo: 2
Ingrese el número de iteraciones: 4
```
### El programa imprimirá algo como esto:
```python
La suma de 3 + 2 es: 5
La resta de 3 - 2 es: 1
La multiplicación de 3 * 2 es: 6
La división de 3 / 2 es: 1.50
El módulo de 3 % 2 es: 1


La suma de 6 + 4 es: 10
La resta de 6 - 4 es: 2
La multiplicación de 6 * 4 es: 24
La división de 6 / 4 es: 1.50
El módulo de 6 % 4 es: 2


La suma de 12 + 8 es: 20
La resta de 12 - 8 es: 4
La multiplicación de 12 * 8 es: 96
La división de 12 / 8 es: 1.50
El módulo de 12 % 8 es: 4


La suma de 24 + 16 es: 40
La resta de 24 - 16 es: 8
La multiplicación de 24 * 16 es: 384
La división de 24 / 16 es: 1.50
El módulo de 24 % 16 es: 8
```
