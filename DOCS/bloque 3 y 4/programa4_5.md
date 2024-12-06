# programa 4_5
"Argumento parametro"
# Explicación del programa
### Definición de la función ``saludar``:
```python
def saludar(nombre, edad):
````
Se define la función ``saludar`` con dos parámetros: ``nombre`` y ``edad``. Los parámetros son como "variables de entrada" para la función, esperando recibir valores cuando se llama.

### Impresión del saludo personalizado:
```python
print(f'\n!Hola, {nombre}¡')
````
Utiliza una f-string para insertar el valor del parámetro ``nombre`` en el saludo. El ``\n`` al principio crea una nueva línea antes del mensaje.

### Impresión de la edad:
```python
print(f'tienes {edad} años.')
````
Utiliza una f-string para insertar el valor del parámetro ``edad`` y mostrar cuántos años tiene la persona.

### Deseo de bienestar:
```python
print('¡Espero que te encuentres bien!\n')
````
Imprime un mensaje genérico deseando que la persona esté bien, con una nueva línea al final para separar el saludo de cualquier siguiente salida.

### Llamadas a la función con argumentos:
```python
saludar('Edinguer', edad=26)
saludar('Chuyito', edad=18)
saludar('terricola', edad=23)
````
Estas líneas llaman a la función ``saludar`` tres veces, cada vez pasando diferentes argumentos (valores reales) para los parámetros ``nombre`` y ``edad``.

### Resultado al ejecutarse:
```python
!Hola, Edinguer¡
tienes 26 años.
¡Espero que te encuentres bien!

!Hola, Chuyito¡
tienes 18 años.
¡Espero que te encuentres bien!

!Hola, terricola¡
tienes 23 años.
¡Espero que te encuentres bien!
```
