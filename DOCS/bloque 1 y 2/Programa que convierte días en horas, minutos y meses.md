# Programa que convierte días en horas, minutos y meses

## Explicación del programa 

 Solicitamos al usuario que ingrese la cantidad de días.
 Usamos la función input() para capturar lo que el usuario escribe y lo convertimos a tipo int,
 ya que la cantidad de días debe ser un número entero.

```dias = int(input("Digite la cantidad de días: "))```

 Calculamos la cantidad de horas equivalentes a los días ingresados.
 Sabemos que un día tiene 24 horas, por lo que multiplicamos los días por 24.
 
```horas = dias * 24```

 Calculamos la cantidad de minutos equivalentes a las horas calculadas.
 Sabemos que una hora tiene 60 minutos, por lo que multiplicamos las horas por 60.
 
```min = horas * 60```

 Calculamos la cantidad de meses aproximados equivalentes a los días ingresados.
 Sabemos que un mes tiene aproximadamente 30 días, por lo que dividimos los días entre 30.
 
```meses = dias / 30```

 Imprimimos el resultado de las horas.
 Convertimos el valor de 'horas' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("La cantidad de horas en esos días es: " + str(horas))```

 Imprimimos el resultado de los minutos.
 Convertimos el valor de 'min' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("La cantidad de minutos en esas horas es: " + str(min))```

 Imprimimos el resultado de los meses.
 Convertimos el valor de 'meses' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("La cantidad de meses en esos días es: " + str(meses))```
