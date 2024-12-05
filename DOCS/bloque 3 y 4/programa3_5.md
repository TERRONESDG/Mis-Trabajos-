# Programa 3_5
Programa para evaluar el nivel de desempeño según la calificación ingresada
# Explicación del programa 
Solicitamos al usuario que ingrese su calificación. Usamos la función `input()` para capturar el valor, y luego lo convertimos a tipo `int` para poder compararlo numéricamente.
```python
calificaciones = int(input("Ingresa tu calificación para evaluar tu desempeño:"))
```

A continuación, se evalúan los diferentes rangos de calificación usando condicionales `if`, `elif` y `else` para determinar el nivel de desempeño:

Si la calificación es menor o igual a 60, el nivel de desempeño será "Insuficiente".
```python
if calificaciones <= 60:
    print("Insuficiente")
```

Si la calificación está entre 70 y 79 (inclusive), el nivel de desempeño será "Suficiente".
```python
elif calificaciones >= 70 and calificaciones <= 79:
    print("Suficiente")
```

Si la calificación está entre 80 y 89 (inclusive), el nivel de desempeño será "Muy bien!".
```python
elif calificaciones >= 80 and calificaciones <= 89:
    print("Muy bien!")
```

Si la calificación está entre 90 y 95 (inclusive), el nivel de desempeño será "Notable!".
```python
elif calificaciones >= 90 and calificaciones <= 95:
    print("Notable!")
```

Si la calificación es mayor que 95, el nivel de desempeño será "Excelente".
```python
else:
    print("Excelente")
```

Finalmente, mostramos un mensaje de agradecimiento por usar el sistema de evaluación.
```python
print("¡Gracias por usar mi sistema de evaluación!")
```
