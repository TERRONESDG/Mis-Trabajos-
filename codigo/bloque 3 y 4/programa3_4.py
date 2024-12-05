#Programa.4 programa que calcule los impuestos
#Elaborado el 29/10/2024
#Elaborado por : Diego Andres Terrones Gonzalez.


ingresos = input("Cuales son sus ingresos:")
ingresos = float(ingresos)

if ingresos <=1000:
     impuesto = ingresos * 0.05

elif ingresos > 1000 and ingresos <=2500:      
     impuesto = ingresos * 0.08

elif ingresos > 2500 and ingresos <= 6000:
     ingresos > ingresos * 0.12
    
else:
     impuestos = ingresos *0.15

salario_total =ingresos - impuesto
print("Tus impuestos son" + str(ingresos) + "y tu salario final es" + str (salario_total))
  