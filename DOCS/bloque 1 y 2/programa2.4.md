# Programa 2.4
Programa que calcula impuestos y muestre un valor
# Explicacion del programa.
```python
def calcular_impuesto(valor, tasa_impuesto):
```
 Definir la función 'calcular_impuesto' que recibe dos parámetros: 'valor' y 'tasa_impuesto'
    
 ``impuesto = valor * (tasa_impuesto / 100)``   Calcula el impuesto multiplicando el valor por la tasa del impuesto (dividida entre 100)
 
 ``return impuesto``   Devuelve el valor del impuesto calculado

### Solicitar al usuario que ingrese el valor y la tasa de impuesto

``valor = float(input("Introduce el valor:"))``   El valor debe ser un número decimal (float)

``tasa_impuesto = float(input("Introduce la tasa de impuesto en %:"))``   La tasa de impuesto debe ser un número decimal (float)


``print(f"El impuesto sobre {valor} con una tasa del {tasa_impuesto}% es: {calcular_impuesto(valor, tasa_impuesto):.2f}\nGracias por usar nuestro sistema!")``
Mostrar el resultado utilizando f-string para formatear el resultado con 2 decimales
