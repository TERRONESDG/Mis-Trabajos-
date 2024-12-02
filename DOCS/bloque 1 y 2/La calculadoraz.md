# Programa 3  
 
## Calculadora: Realiza operaciones aritméticas según la selección del usuario.

### Definimos la función principal que contiene toda la lógica del programa.


  Imprimimos un mensaje de bienvenida al usuario.
    
   ```def calculadora():```
   ``` print("Calculadora Básica") ``` 
   
  Mostramos al usuario las operaciones que están disponibles.
    
     ``` print("Operaciones disponibles: suma (+), resta (-), multiplicación (*), división (/)") ``` 

  Solicitamos al usuario que ingrese el primer número.
   La función input() captura lo que el usuario escribe y lo convertimos a tipo float
   para que el programa pueda manejar números decimales.
   
   ```  num1 = float(input("Ingresa el primer número: ")) ``` 

  Solicitamos el segundo número al usuario y realizamos el mismo procedimiento.
  
    ```num2 = float(input("Ingresa el segundo número: "))```
    
  Solicitamos al usuario que elija la operación que desea realizar.
  Esto se hace ingresando uno de los símbolos: +, -, *, /.
  
  ```  operacion = input("Ingresa la operación (+, -, *, /): ") ``` 

  Usamos una estructura condicional para determinar qué operación debe ejecutarse.
   Si el usuario elige "+", realizamos una suma.
   
   ```if operacion == "+": ``` 
   
  Sumamos los dos números ingresados.
  
   ```resultado = num1 + num2```
   
  Mostramos el resultado al usuario.
  
 ```print(f"El resultado es: {resultado}")```

Si el usuario elige "-", realizamos una resta.

   ```elif operacion == "-":```
     
  Restamos el segundo número del primero.
  
   ```resultado = num1 - num2```

  Mostramos el resultado al usuario.
  
   ``` print(f"El resultado es: {resultado}") ```

   Si el usuario elige "*", realizamos una multiplicación.
   
  ```elif operacion == "*":```
  
  Multiplicamos los dos números.
      
  ``` resultado = num1 * num2 ```
  
  Mostramos el resultado al usuario.
     
  ```print(f"El resultado es: {resultado}") ``` 


   Si el usuario elige "/", realizamos una división. 
   
  ```elif operacion == "/": ```

  Antes de realizar la división, verificamos si el divisor (num2) es diferente de cero.
     
   ```if num2 != 0:```

   Dividimos el primer número entre el segundo.
  
   ```resultado = num1 / num2 ``` 

   Mostramos el resultado al usuario.
   
  ```print(f"El resultado es: {resultado}") ```
  
  else:
        
   Si el divisor es cero, mostramos un mensaje de error porque no se puede dividir entre cero.
   
  ```print("Error: No se puede dividir entre cero.")```
  
  else:
   
  Si el usuario ingresa un símbolo que no es válido, mostramos un mensaje de error.
       
  ```print("Operación no válida.")```

 Llamamos a la función principal para que se ejecute el programa.
 
```calculadora()```
