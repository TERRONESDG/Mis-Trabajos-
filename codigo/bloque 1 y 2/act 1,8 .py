#Programa.8 calcule las horas, minutos y mese que han pasado al ingresar una cantidad de dias
#Fecha de elaboraciÓn: 20210/10/16
#Elaborado por: ANDREA GUADALUPE JIMENEZ CARDENAS

dias = float (input("Ingresa el numero de dias:"))
horas = dias * 24
minutos = horas * 60
meses = dias / 30

print ("El resultado de horas es:" , str (horas))
print ("El resultado de minutos es:" , str (minutos))
print ("El resultado de meses es:" , str (meses))
