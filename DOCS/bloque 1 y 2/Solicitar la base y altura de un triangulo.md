# Programa que calcula el área y base de un triángulo

## Explicación del programa 

 Solicitamos al usuario que ingrese la medida de la base del triángulo.
 Usamos la función input() para capturar lo que el usuario escribe y lo convertimos a tipo float,
 ya que la base puede ser un número decimal.
 
```base = float(input("Cuánto mide la base: "))```

 Solicitamos al usuario que ingrese la medida de la altura del triángulo.
 También convertimos el valor ingresado a tipo float para permitir números decimales.
 
```altura = float(input("Cuánto mide la altura: "))```

 Calculamos el área del triángulo utilizando la fórmula:
 Área = (base * altura) / 2
 
```area = base * altura / 2```

 Imprimimos el resultado del cálculo del área.
 Convertimos el valor de 'area' a cadena con str() para poder concatenarlo con el mensaje.
 
```print("El área de este triángulo es: " + str(area))```
