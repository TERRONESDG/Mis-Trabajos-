# Programa 4_4
Definición de función
# Explicación del Código

Este código define una función en Python llamada `saludar`, que toma un parámetro `nombre` y luego imprime un mensaje personalizado utilizando ese nombre.

### Código


Definición de la función saludar:
```python
def saludar(nombre):
````
Se define la función ``saludar`` que acepta un argumento llamado ``nombre``.

### Impresión del saludo personalizado:
```python
print(f'\n!Hola, {nombre}¡')
````
Utiliza una f-string para insertar el valor de ``nombre`` en el saludo. El ``\n`` al principio crea una nueva línea antes del mensaje. Por ejemplo, si ``nombre`` es "Edinguer", el mensaje será ``!Hola, Edinguer¡``.

### Pregunta sobre el estado de la persona:
```python
print(f'Como estás?')
```
Imprime "¿Cómo estás?", sin utilizar f-string ya que no hay variables.

### Deseo de bienestar:
```python
print('¡Espero que te encuentres bien!\n')
````
Imprime un mensaje genérico deseando que la persona esté bien, con una nueva línea al final para separar el saludo de cualquier siguiente salida.

### Llamadas a la función:
```python
saludar('Edinguer')
saludar("Chuyito")
saludar("terricola")
```
Estas líneas llaman a la función ``saludar`` tres veces con diferentes nombres como argumentos (``'Edinguer'``, ``'Chuyito'``, y ``'terricola'``), generando tres saludos personalizados.

### Resultado al ejecutarse:
```python
!Hola, Edinguer¡
Como estás?
¡Espero que te encuentres bien!

!Hola, Chuyito¡
Como estás?
¡Espero que te encuentres bien!

!Hola, terricola¡
Como estás?
¡Espero que te encuentres bien!
```







