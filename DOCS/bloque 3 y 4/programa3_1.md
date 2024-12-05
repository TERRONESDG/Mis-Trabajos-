# Programa3_1
Elife
# Expicación del programa


Programa para identificar el tipo de mascota según lo que escribe el usuario.

Solicitamos al usuario que ingrese el tipo de mascota que tiene.
Usamos la función input() para capturar lo que el usuario escribe. El valor ingresado
se almacena en la variable 'nombre'.

``` python
nombre = input("Ingresa el tipo de mascota que tienes: ")
````

Verificamos si el texto ingresado contiene la palabra "perro".
Usamos el operador 'in' para buscar si la palabra "perro" está presente en la cadena ingresada.
```python
if "perro" in nombre:
```
   Si se encuentra "perro" en el texto, mostramos un mensaje indicando que es un perro.
   
```python
    print("Es un perro")
```

Verificamos si el texto ingresado contiene la palabra "gato".
Usamos otra condición 'elif' para buscar si la palabra "gato" está presente en la cadena ingresada.
```python
elif "gato" in nombre:
````
   Si se encuentra "gato" en el texto, mostramos un mensaje indicando que es un gato.
   ```python 
    print("Es un gato")
````
Si no se encuentra ni "perro" ni "gato" en el texto ingresado,
mostramos un mensaje indicando que la mascota es desconocida.
```python
else:
    print("Mascota desconocida")

````
