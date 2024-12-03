# Programa 2.9
Programa que calcule el costo total de un número de artículos
# Explicación del programa.
 Solicita al usuario ingresar la cantidad de artículos comprados y la convierte en un número entero.
 ```python
cantidad = int(input("¿Cuantos articulos compro?")) 
```
Condición IF: Si la cantidad comprada es mayor a 3, se aplica un precio especial por unidad.
```python
if cantidad > 3:
```
 Si la cantidad es mayor a 3, cada artículo cuesta $30.
```python
    total = cantidad * 30  
```
Si la cantidad es 3 o menor, cada artículo cuesta $45.
```python
else:
    total = cantidad * 45
```
 Imprime el total a pagar, convirtiendo el número total a una cadena (str) para concatenarlo con el texto.
 ```python
print("EL TOTAL A PAGAR ES: $" + str(total))
```
Mensaje de despedida con un emoji de carita feliz.
```python
print("Gracias por su compra !Que tengas un buen día¡ \U0001F600")
```
