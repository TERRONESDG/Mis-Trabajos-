# programa 4_6
Programa que realice una función para realizar operaciones matemáticas básicas 
# Explicación del programa

### Definición de la función operaciones:
```python
def operaciones(num1, num2, digitos):
```
Esta función toma tres parámetros: num1 y num2 son los dos números con los que se realizarán las operaciones, y digitos es el número de decimales que se deben mostrar en la división y el módulo.

### Realización de las operaciones matemáticas:

Suma:
```python
suma = num1 + num2
```
Se realiza la suma de los dos números.

### Resta:
```python
resta = num1 - num2
```
Se realiza la resta de los dos números.

### Multiplicación:
```python
multiplicacion = num1 * num2
```
Se realiza la multiplicación de los dos números.

### División:
```python
division = float(num1 / num2)
```
Se realiza la división de los dos números, y se convierte a un tipo float para asegurar que el resultado sea un número decimal.

### Módulo:
```
modulo = num1 % num2
```
Se calcula el módulo de num1 y num2, es decir, el residuo de la división.

### Impresión de los resultados: 
Se imprime el resultado de cada operación. En la división y el módulo, se especifica que el número de decimales que se debe mostrar es determinado por el parámetro digitos.

```python
print(f'La división de {num1} / {num2} es: {division:.{digitos}f}')
```
Esto asegura que la división se imprima con la cantidad de decimales que el usuario haya especificado.

### Solicitar datos al usuario:

```python
num1 = int(input('Ingrese el primer número: '))    
num2 = int(input('Ingrese el segundo número: '))    
digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))
````
El código solicita al usuario que ingrese los valores para num1, num2, y digitos.


### Llamadas a la función operaciones:
```python
operaciones(num1, num2, digitos)
operaciones(140, 8, 5)
````
Llama a la función operaciones con los valores ingresados por el usuario y luego con los valores 140 y 8 para mostrar un ejemplo adicional.

### Ejemplo de salida:
```python
Ingrese el primer número: 10
Ingrese el segundo número: 3
Ingrese la cantidad de decimales a mostrar en la división y módulo: 2
La suma de 10 + 3 es: 13
La resta de 10 - 3 es: 7
La multiplicación de 10 * 3 es: 30
La división de 10 / 3 es: 3.33
El módulo de 10 % 3 es: 1


La suma de 140 + 8 es: 148
La resta de 140 - 8 es: 132
La multiplicación de 140 * 8 es: 1120
La división de 140 / 8 es: 17.50000
El módulo de 140 % 8 es: 4
```





