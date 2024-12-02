# Programa 4
 Programa que solicita dos números al usuario, realiza operaciones matemáticas y muestra los resultados.

# Línea 1 y 2:
Se solicita al usuario que ingrese dos números. Usamos la función input() para capturar los datos
y los convertimos a tipo float para permitir operaciones matemáticas.
```python
num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
```

# Realizamos las operaciones básicas:
```python
suma = num1 + num2
res = num1 - num2
multi = num1 * num2
div = num1 / num2
```

# Imprimimos los resultados:
```python
print("La suma de esos 2 números da como resultado: " + str(suma))
print("La resta de esos 2 números da como resultado: " + str(res))
print("La multiplicación de esos 2 números da como resultado: " + str(multi))
print("La división de esos 2 números da como resultado: " + str(div))
```
