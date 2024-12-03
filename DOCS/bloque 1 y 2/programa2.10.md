# programa 2.10
Revisar si puede er una película y si es mayor de edad
# Explicación del programa.

Solicita al usuario su edad y la convierte a un número entero.
```python
edad = int(input("¿Cuántos años tienes?")) 
```
Pregunta si compró la película. El usuario responde con 0 (No) o 1 (Sí).
```python
compra = int(input("Compraste la película?\n0-NO\n1-SI\n"))  
```

Condición principal: Verifica si la edad del usuario es mayor o igual a 18.

``if edad >= 18:``

  Si tiene 18 años o más, verifica si compró la película (compra == 1).
  
  ``if compra == 1:``
  
  ``print("Puede ver la película")``   Si la edad es mayor o igual a 18 y compró la película, se imprime este mensaje.
        
 Si la edad es menor de 18, imprime este mensaje.
```python
else:
    print("Vete a hacer la tarea !Mocoso¡") 
````
``print("¡Gracias por usar Netflix!")``   Mensaje de despedida que se imprime al final del programa.
