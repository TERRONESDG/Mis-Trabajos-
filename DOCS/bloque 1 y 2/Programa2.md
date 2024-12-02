# Programa 2
 Programa que solicite el nombre y lo imprime en un mensaje personalizado

 # Explicación del programa.

En la línea 1 usamos la función ``input()``. 

```python
nombre = input("Ingresa tu nombre:")
```
Esta función sirve para pedir al usuario que ingrese un dato por teclado. 
El texto dentro de los paréntesis ``("Ingresa tu nombre:")`` es un mensaje que se muestra al usuario para indicarle qué debe ingresar.


En la línea 2 usamos la función ``print()``. 

```python
print("Hola " + nombre + ", ¡qué bonito es tu nombre!")
```

Aquí imprimimos un mensaje personalizado utilizando el valor que el usuario introdujo.
El operador "+" se utiliza para concatenar (unir) cadenas de texto con la variable ``'nombre'``.
Esto muestra un mensaje que combina texto fijo con el nombre ingresado.
