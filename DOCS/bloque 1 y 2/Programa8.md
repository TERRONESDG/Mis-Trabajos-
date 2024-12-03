# Programa 8
Calcule las horas, minutos y meses que han pasado ingresando una cantidad de días
# Explicación del programa

### Solicitar al usuario que ingrese el número de días
```python
dias = float(input("Ingresa el número de días:"))
```
Convierte la entrada a un número decimal (float).

### Calcular la cantidad de horas, minutos y meses basados en el número de días ingresados

```python
horas = dias * 24 
```
 1 día tiene 24 horas, por lo que multiplicamos los días por 24.

```python
minutos = horas * 60
```
 1 hora tiene 60 minutos, por lo que multiplicamos las horas por 60.

```python
meses = dias / 30  
```
 Aproximación de que un mes tiene 30 días, por lo que dividimos los días entre 30.

## Mostrar los resultados
``print("El resultado de horas es:", str(horas))``   Imprime el número de horas, convierte el resultado a cadena.

``print("El resultado de minutos es:", str(minutos))``   Imprime el número de minutos, convierte el resultado a cadena.

``print("El resultado de meses es:", str(meses))``   Imprime el número de meses, convierte el resultado a cadena.
