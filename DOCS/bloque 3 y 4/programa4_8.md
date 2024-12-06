# Prorama 4_8
Agregar a p-7 un while ,hasta que se ingrese salir con la función .lower
# Explicación del Código
Definición de la Función operaciones: La función realiza operaciones básicas (suma, resta, multiplicación, división y módulo) y muestra los resultados formateados según la cantidad de decimales indicada.

### Ciclo while:
```python
while True:
````
Este es un bucle infinito que solo se detiene cuando el usuario escribe "salir". Dentro del bucle, el programa solicita datos al usuario, ejecuta las operaciones y permite repetirlas o salir.

### Solicitud de Datos al Usuario:
```python
num2 = int(input('Ingrese el segundo número: '))
num1 = int(input('Ingrese el primer número: '))
digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))
iteraciones = int(input('Ingrese el número de iteraciones: '))
```
Se solicita al usuario los números, la cantidad de decimales y el número de iteraciones para las operaciones.

### Ciclo for:
```python
for i in range(iteraciones):
    operaciones(num1, num2, digitos)
    num1 *= 2
    num2 *= 2
```
### Tabla de iteración
| Iteración | num1 | num2 | Suma  | Resta | Multiplicación | División | Módulo |
|-----------|------|------|-------|-------|-----------------|----------|--------|
|     1     |   3  |   5  |   8   |  -2   |       15        |   0.60   |    3   |
|     2     |   6  |  10  |  16   |  -4   |       60        |   0.60   |    6   |
|     3     |  12  |  20  |  32   |  -8   |      240        |   0.60   |   12   |

Este ciclo se ejecuta tantas veces como el valor ingresado en iteraciones. En cada iteración:

Se llaman las operaciones con los valores actuales de num1 y num2.
Los valores de num1 y num2 se duplican para la próxima iteración.

### Control de Salida:
```python
respuesta = input("¿Desea realizar otra operación? (Escriba 'salir' para terminar o presione Enter para continuar): ").lower()
if respuesta == "salir":
    print("¡Hasta luego!")
    break
```
Después de completar las iteraciones, el programa pregunta al usuario si desea continuar o salir. Si la respuesta, convertida a minúsculas con .lower(), es "salir", el programa termina.

### Ejemplo de Ejecución
```python
Ingrese el segundo número: 2
Ingrese el primer número: 3
Ingrese la cantidad de decimales a mostrar en la división y módulo: 2
Ingrese el número de iteraciones: 2
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


¿Desea realizar otra operación? (Escriba 'salir' para terminar o presione Enter para continuar): salir
¡Hasta luego!
````
### Características Adicionales
El programa es robusto y flexible, ya que permite al usuario realizar múltiples operaciones sin necesidad de reiniciarlo.
Se utiliza .lower() para asegurar que la entrada sea insensible a mayúsculas y minúsculas.
Incluye un mecanismo claro para salir del ciclo (break).
