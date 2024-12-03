# Programa 5
 La calculadora

# Explicación del programa

 Solicitar al usuario que ingrese dos números enteros
```python
num1 = int(input("Ingresa el primer valor:"))  
num2 = int(input("Ingresa el segundo número:"))  
```
``int(input())``: Convierte la entrada del usuario a un número entero. Si no se puede convertir (por ejemplo, si el usuario escribe texto), el programa generará un error.



### Realizar las operaciones matemáticas
``suma = num1 + num2``  
``resta = num1 - num2``  
``multiplicacion = num1 * num2``   
``division = num1 / num2`` 

En la primera suma los dos números ingresados.

En la segunda resta el segundo número al primero.

En la Tercera multiplica los dos números.

Em la cuarta divide el primer número entre el segundo.



# Imprimir los resultados de las operaciones
print("El valor de la suma es: " + str(suma))  # Muestra el resultado de la suma.
print("El valor de la resta es: " + str(resta))  # Muestra el resultado de la resta.
print("El valor de la multiplicación es: " + str(multiplicacion))  # Muestra el resultado de la multiplicación.
print("El valor de la división es: " + str(division))  # Muestra el resultado de la división.
