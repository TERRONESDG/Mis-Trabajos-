# Programa 4_10

# Explicación del programa

Este programa tiene como objetivo verificar si un número ingresado por el usuario entre 10 y 99 es un número primo. La funcionalidad se implementa en dos funciones principales: es_primo y verificar_primo.

1. Función es_primo(numero)
Esta función toma un número y determina si es primo. Un número primo es aquel que solo tiene dos divisores: 1 y él mismo.

## Lógica dentro de la función:
### Condición inicial:
``` python
if numero < 2:
    return False
```
Si el número es menor que 2, la función retorna False porque, por definición, los números menores que 2 no pueden ser primos. Esto se aplica para números como 0 y 1.

### Verificación de divisibilidad:
``` python
for i in range(2, int(math.sqrt(numero)) + 1):
    if numero % i == 0:
        return False
```
### Tabla de iteración 
| Iteración | i   | número % i | ¿Es divisible? | ¿Es primo? |
|-----------|-----|------------|----------------|------------|
|     1     |  2  |     1      |      No        |   True     |
|     2     |  3  |     1      |      No        |   True     |
|     3     |  4  |     1      |      No        |   True     |
|     4     |  5  |     4      |      No        |   True     |
|     5     |  6  |     1      |      No        |   True     |
|     6     |  7  |     0      |      Sí        |   Fals


Este bloque de código usa un bucle for para verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número (sqrt(numero)). ¿Por qué hasta la raíz cuadrada? Porque si un número tiene un divisor mayor que su raíz cuadrada, entonces también tendría uno menor, por lo que no es necesario verificar más allá de la raíz cuadrada.

Si el número es divisible por algún valor de i (es decir, numero % i == 0), entonces no es un número primo, y la función retorna False.
Si el número no tiene divisores:
```python
return True
````
Si el número no fue divisible por ninguno de los valores probados en el rango, se considera un número primo y la función devuelve True.

## Función verificar_primo()
Esta es la función principal que interactúa con el usuario. Solicita un número, verifica si está en el rango válido (entre 10 y 99), y luego llama a la función es_primo() para determinar si el número es primo o no.

Lógica dentro de la función:
Solicitud del número:
```python
numero_usuario = int(input("Ingrese un número entre 10 y 99: "))
El programa pide al usuario que ingrese un número y lo convierte a un valor entero (int).
```

### Comprobación de rango:
```python
if 10 <= numero_usuario <= 99:
```
Verifica si el número ingresado está dentro del rango válido, que es entre 10 y 99.

Si el número está dentro del rango, se procede a comprobar si es primo mediante la función es_primo(numero_usuario).
Si el número no está en el rango, se muestra un mensaje solicitando al usuario que ingrese un número dentro del rango permitido

### Verificación de la primalidad:
```python
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")
```
Llama a la función es_primo(), pasando el número ingresado por el usuario. Si es_primo() devuelve True, el número es primo; de lo contrario, no lo es.

### Llamada a la función verificar_primo()
Al final del código, la función verificar_primo() es llamada para iniciar el proceso.
```python
verificar_primo()
```
Esta llamada hace que el programa ejecute la lógica de pedir al usuario un número, verificar si está en el rango, y luego verificar si es primo.

### Ejemplo de Ejecución
```python
Supongamos que el usuario ingresa el número 37:

El número es verificado para asegurarse de que está en el rango de 10 a 99.
La función es_primo(37) es llamada.
El bucle dentro de es_primo verificará si 37 es divisible entre 2, 3, 4, 5 (ya que la raíz cuadrada de 37 es aproximadamente 6.08).
Ninguno de estos números divide a 37 de manera exacta, por lo que la función retorna True.
El mensaje "37 es un número primo." es mostrado.
```
