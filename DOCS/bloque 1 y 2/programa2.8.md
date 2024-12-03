# Programa 2.8
Calificaciones aprobo o desaprobó 
# Explicación del programa.

 Solicita la calificación y la convierte a float (número decimal).

```python
num1 = float(input("ingresa tu primer calificación:")) 
num2 = float(input("ingresa tu segunda calificación:"))  
num3 = float(input("ingresa tu tercera calificación:"))  
num4 = float(input("ingresa tu cuarta calificacion:"))  
num5 = float(input("ingresa tu quinta calificacion:"))  
num6 = float(input("ingresa tu sexta calificacion:"))  
```

Calcula el promedio de las 6 calificaciones
```python
calificaciones = (num1 + num2 + num3 + num4 + num5 + num6) / 6 
```
Suma todas las calificaciones y las divide entre 6 para obtener el promedio.

Si el promedio de las calificaciones es mayor o igual a 70, se considera que aprobó.
```python
if calificaciones >= 70:
````
``print("Aprobaste tus materias... !FELICIDADES¡")``  Si el promedio es mayor o igual a 70, imprime este mensaje de éxito.

else:
    ``print("Desaprobaste tus materias... Vuelve a intentarlo !si se puede¡")``   Si el promedio es menor que 70, imprime este mensaje de aliento.
