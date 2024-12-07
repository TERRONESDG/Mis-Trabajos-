#programa 8: agregar un ciclo while a p-7
#Fecha de elaboraciÓn: 14/11/2024
#Elaborado por : Diego Andres Terrones Gonzalez.


def operaciones(num1, num2, digitos): 
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicacion de {num1} * {num2} es: {multiplicacion}')
    print(f'La division de {num1} / {num2} es: {division:.{digitos}f}')
    print(f'El modulo de {num1} % {num2} es: {modulo}\n\n')

# Ciclo principal del programa
while True:
    # Solicitar datos al usuario
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    digitos = int(input('Ingrese la cantidad de decimales a mostrar en la division: '))
    cantidad = int(input("¿Cuántas veces deseas realizar las operaciones? "))

    # Repetir las operaciones según lo indicado por el usuario
    for _ in range(cantidad):
        operaciones(num1, num2, digitos)

    # Preguntar al usuario si desea continuar o salir
    respuesta = input("¿Quieres realizar más operaciones? (escribe 'salir' para terminar o presiona Enter para continuar): ")
    if respuesta.lower() == "salir":
        print("¡Hasta luego!")
        break
