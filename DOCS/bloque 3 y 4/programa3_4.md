# Programa 3_4
Programa para calcular impuestos según los ingresos utilizando `if`, `elif` y `else`
# Explicación del programa
Solicitamos al usuario que ingrese sus ingresos. Usamos la función `input()` para capturar el valor ingresado, y luego lo convertimos a tipo `float` para poder realizar las operaciones matemáticas.
```python
ingresos = input("¿Cuáles son sus ingresos?")
ingresos = float(ingresos)
```

A continuación, comenzamos a aplicar las condiciones para calcular los impuestos según los rangos de ingresos:

Si los ingresos son menores o iguales a 1000, el impuesto se calcula multiplicando los ingresos por 0.05.
```python
if ingresos <= 1000:
    impuesto = ingresos * 0.05
```

Si los ingresos son mayores a 1000 y menores o iguales a 2500, el impuesto será del 8% sobre los ingresos.
```python
elif ingresos > 1000 and ingresos <= 2500:
    impuesto = ingresos * 0.08
```

Si los ingresos son mayores a 2500 y menores o iguales a 6000, el impuesto se calcula con una tasa del 12%.
```python
elif ingresos > 2500 and ingresos <= 6000:
    impuesto = ingresos * 0.12
```

Si los ingresos superan los 6000, el impuesto se calcula con una tasa del 15%.
```python
else:
    impuesto = ingresos * 0.15
```

Finalmente, calculamos el salario total, que es el resultado de restar el impuesto de los ingresos, y mostramos el impuesto y el salario final.
```python
salario_total = ingresos - impuesto
print("Tus impuestos son " + str(impuesto) + " y tu salario final es " + str(salario_total))
```
