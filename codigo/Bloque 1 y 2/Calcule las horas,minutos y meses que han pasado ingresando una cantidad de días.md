#Calcule las horas,minutos y meses que han pasado ingresando una cantidad de días

## Programa ue calculael numero de minutos, horas y meses, dado el numero de dias por el usuario
## Fecha: 16710/2024
## Elaborado por: Diego Andres Terrones Gonzalez

```python
dias = int(input("Digite la cantidad de dias: "))
horas = dias * 24
min = horas * 60
meses = dias / 30
print("La cantidad de horas en esos dias es: "+str(horas))
print("La cantidad de minutos en esas horas es: "+str(min))
print("La cantidad de meses en esos dias es: "+str(meses))
```

