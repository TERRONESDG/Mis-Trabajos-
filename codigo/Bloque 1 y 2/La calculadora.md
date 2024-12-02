# Programa 5: La calculadora

``` python 
# Calculadora
def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles: suma (+), resta (-), multiplicación (*), división (/)")

    # Solicitar números al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Solicitar la operación
    operacion = input("Ingresa la operación (+, -, *, /): ")

    # Realizar la operación
    if operacion == "+":
        print(f"El resultado es: {num1 + num2}")
    elif operacion == "-":
        print(f"El resultado es: {num1 - num2}")
    elif operacion == "*":
        print(f"El resultado es: {num1 * num2}")
    elif operacion == "/":
        if num2 != 0:
            print(f"El resultado es: {num1 / num2}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Operación no válida.")

# Ejecutar la calculadora
calculadora()
```
