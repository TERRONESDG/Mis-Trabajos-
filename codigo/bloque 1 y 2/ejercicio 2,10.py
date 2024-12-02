#Programa.10 Revisar si puedes ver una pelicula y eres mayor de edad 
#Fecha de elaboraciÓn: 20210/10/22
#Elaborado por: ANDREA GUADALUPE JIMENEZ CARDENAS

edad = int(input("¿cuantos años tienes?"))
compra = int(input("Compraste la pelicula?\n0-NO\n1-SI\n"))


if edad >=18:
     if compra == 1:
          print("Puede ver la pelicula")

else:
     print("Vete a hacer la tarea !Mocoso¡")

print("!Gracias por usar Netflix¡")


