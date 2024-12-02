# Programa que calcula el área y el perímetro de un círculo
## Explicación del programa.

 Solicitamos al usuario que ingrese el valor del radio del círculo.
 Usamos la función input() para capturar lo que el usuario escribe y lo convertimos a tipo float,
 ya que el radio puede ser un número decimal.
 
```radio = float(input("Ingresa el valor del radio: "))```

 Calculamos el área del círculo utilizando la fórmula:
 Área = π * radio^2. Usamos el valor aproximado de π como 3.1416.
 
```area = 3.1416 * radio ** 2``` radio ** 2 es lo mismo que radio al cuadrado.

 Calculamos el perímetro del círculo utilizando la fórmula:
 Perímetro = 2 * π * radio. También usamos el valor aproximado de π.
 
```perimetro = 3.1416 * 2 * radio```

 Imprimimos el resultado del cálculo del área.
 Convertimos el valor de 'area' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("El área del círculo es: " + str(area))```

 Imprimimos el resultado del cálculo del perímetro.
 Convertimos el valor de 'perimetro' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("El perímetro del círculo es: " + str(perimetro))```
