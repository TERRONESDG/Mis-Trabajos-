# Programa 7
Que pida el radio de un circulo y saque sus valores
# Explicación del programa

### Solicitar al usuario que ingrese el valor del radio del círculo

```python
radio = float(input("Introduce el valor del radio del círculo:")) 
```
El ``float(imput()``convierte la entrada a un número decimal (float).


### Calcular el perímetro de la circunferencia utilizando la fórmula: 2 * pi * radio

```python
perimetro = 2 * 3.1416 * radio  
```
La constante pi es aproximada a 3.1416.

### Calcular el área del círculo utilizando la fórmula: pi * radio^2
```python
area = 3.1416 * radio ** 2  
```
Radio ** 2 significa radio al cuadrado.

### Mostrar los resultados utilizando f-strings para formatear la salida
```python
print(f"El perímetro del círculo es: {perimetro}")
```
Muestra el perímetro calculado.
```python
print(f"El área del círculo es: {area}")  
```
Muestra el área calculada.

