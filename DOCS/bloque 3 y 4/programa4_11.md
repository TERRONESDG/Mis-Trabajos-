# Programa 4_11
Agregue p-10 un ciclo while para que se repita el programa
# Explicación del programa
### Importación de la biblioteca math:
```python
import math
```
Se importa el módulo math para usar su función sqrt() que calcula la raíz cuadrada de un número, lo cual optimiza la verificación de primalidad.
### Función es_primo:
```python
def es_primo(numero):
    if numero < 2:
        return False   
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False   
    return True
```
Comprobación si el número es menor que 2: Si el número es menor que 2 (como 0 o 1), no es primo, por lo que la función devuelve False.
Verificación de divisibilidad: Usa un ciclo for para verificar si el número es divisible por algún número desde 2 hasta la raíz cuadrada de ese número. Si encuentra algún divisor, el número no es primo y la función devuelve False. Si no encuentra divisores, retorna True, indicando que el número es primo.
# Ciclo while:
```python

while True:
    entrada = input("Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: ").lower()  
    if entrada == "salir":
        print("¡Hasta luego, gracias por usar mi programa!")
        break
```
Ciclo infinito: El ciclo while ejecutará el código dentro de él indefinidamente hasta que se ingrese "salir". Esto permite que el programa siga pidiendo números y verifique su primalidad sin reiniciar el programa.
Si el usuario ingresa "salir", el programa imprime un mensaje de despedida y el ciclo se termina con break.
### Entrada del usuario y manejo de errores:
``` python
try:
    numero_usuario = int(entrada)
    if 10 <= numero_usuario <= 99:
        if es_primo(numero_usuario):
            print(f"{numero_usuario} es un número primo.")
        else:
            print(f"{numero_usuario} no es un número primo.")
    else:
        print("Por favor, ingrese un número entre 10 y 99.")
except ValueError:
    print("Por favor, ingrese un número válido o 'salir' para terminar.")
```
### Conversión de la entrada: 
El código intenta convertir la entrada a un número entero usando int(). Si la conversión falla (por ejemplo, si el usuario ingresa texto o un número no válido), se captura el error mediante except ValueError y se le pide al usuario que ingrese un número válido.
### Comprobación de rango: 
Si la entrada es un número válido, el código verifica si está entre 10 y 99. Si está dentro de este rango, se llama a la función es_primo() para determinar si el número es primo. Si no está en el rango, se le solicita al usuario ingresar un número dentro de los límites.
### Resultado de primalidad: 
Si el número es primo, se le informa al usuario que es un número primo. Si no lo es, se le indica que no es un número primo.

### Ejemplo de Ejecución
El programa pide al usuario que ingrese un número entre 10 y 99 o "salir" para terminar.
Si el usuario ingresa un número, el programa verifica si es primo o no y muestra el resultado.
Si el usuario ingresa algo que no es un número válido, el programa lo avisa.
El ciclo se repite hasta que el usuario ingresa "salir".

### Ejemplo de la Interacción
```python


Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 37
37 es un número primo.



Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 40
40 no es un número primo.


Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 105
Por favor, ingrese un número entre 10 y 99.

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: salir
¡Hasta luego, gracias por usar mi programa!
```
