#programa 9: Deducir si un numero entre 10 y 99 es primo
#Fecha de elaboraciÓn: 15/11/2024
#Elaborado por : Diego Andres Terrones Gonzalez.


num = int(input("Ingrese un numero: "))
if num >= 10 and num <= 99:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break  

    if es_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
else:
    print("El número ingresado no está en el rango de 10 a 99.")



    