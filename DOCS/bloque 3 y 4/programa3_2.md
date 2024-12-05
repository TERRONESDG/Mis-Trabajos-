# Programa 3_2
Programa para comparar dos números ingresados por el usuario
# Explicación del programa

Solicitamos al usuario que ingrese el primer número.
Usamos la función input() para capturar lo que escribe el usuario.
Convertimos el valor ingresado a un número entero utilizando int().
```python
num1 = int(input("Ingresa el primer número: "))
```
Solicitamos al usuario que ingrese el segundo número.
También convertimos este valor a un número entero.
```python
num2 = int(input("Ingresa el segundo número: "))
````
Comparación entre los dos números ingresados.
Evaluamos si el primer número es mayor que el segundo.
```python
if num1 > num2:
    print(str(num1) + "\nEs mayor que " + str(num2))
```
Evaluamos si ambos números son iguales.
```python
elif num1 == num2:
    print(str(num1) + "\nEs igual que " + str(num2))
```
Si ninguna de las condiciones anteriores se cumple, significa que el primer número es menor que el segundo.
```python
else:
    print(str(num1) + "\nEs menor que " + str(num2))
```
Mensaje final de agradecimiento.
Este mensaje se imprime siempre, sin importar qué comparación fue verdadera.
```python
print("¡Gracias por usar mi programa!")
```

