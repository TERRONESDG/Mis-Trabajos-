#  imprimir distinto tipos de datos..


### Este programa imprimira los distintos de datos que vimos en clase:

```python
# Alfanumérico (string)
cadenas = ["juan", "pedro", "chuy"]
print(cadenas)  # Muestra la lista completa
print(cadenas[1])  # Imprime el segundo elemento: "pedro"
print(type(cadenas))  # Imprime el tipo de "cadenas" (lista)
print(type(cadenas[1]))  # Imprime el tipo del segundo elemento (str)

# Enteros
enteros = [5, 4, 8]
print(enteros)  # Muestra la lista de enteros
print(enteros[0])  # Imprime el primer elemento: 5
print(type(enteros))  # Imprime el tipo de "enteros" (lista)
print(type(enteros[0]))  # Imprime el tipo del primer elemento (int)

# Flotantes
flotantes = [3.14, 2.71, 1.61]
print(flotantes)  # Muestra la lista de flotantes
print(flotantes[0])  # Imprime el primer elemento: 3.14
print(type(flotantes))  # Imprime el tipo de "flotantes" (lista)
print(type(flotantes[0]))  # Imprime el tipo del primer elemento (float)

# Binarios
binarios = [0b1010, 0b1101, 0b1111]
print(binarios)  # Muestra la lista de números binarios
print(binarios[0])  # Imprime el primer número binario (equivalente a 10 en decimal)
print(type(binarios))  # Imprime el tipo de "binarios" (lista)
print(type(binarios[0]))  # Imprime el tipo del primer número binario (int)

# Listas
listas = [cadenas, enteros, flotantes, binarios]  # Lista que mezcla todos los tipos anteriores
print(listas)  # Muestra la lista completa
print(listas[2])  # Imprime el tercer elemento de la lista (flotantes)
print(type(listas))  # Imprime el tipo de "listas" (lista)
print(type(listas[2]))  # Imprime el tipo del tercer elemento (lista de flotantes)

```
## DESCRIPCION DEl PROGRAMA:

## 1. Alfanumérico (string)
En este programa, la lista cadenas guarda tres cadenas de texto. El código print(cadenas) muestra la lista completa, mientras que print(cadenas[1]) imprime el segundo elemento de la lista, "pedro". Luego, type(cadenas) y type(cadenas[1]) muestran que cadenas es de tipo lista y que el segundo elemento es una cadena de texto (str).

## 2. Enteros
La lista enteros guarda tres números enteros. El código print(enteros) imprime la lista completa de números enteros, y print(enteros[0]) imprime el primer elemento de la lista, 5. Además, type(enteros) y type(enteros[0]) muestran que enteros es una lista y que el primer elemento es un número entero (int).

## 3. Flotantes
La lista flotantes contiene tres números decimales. print(flotantes) muestra la lista completa, y print(flotantes[0]) imprime el primer valor flotante, 3.14. type(flotantes) y type(flotantes[0]) indican que flotantes es una lista y que el primer valor es de tipo flotante (float).

## 4. Binarios
En este caso, la lista binarios guarda números en formato binario. print(binarios) imprime la lista de números binarios, y print(binarios[0]) muestra el primer valor binario, que en decimal es 10. Los códigos type(binarios) y type(binarios[0]) indican que binarios es una lista y que el primer valor binario es de tipo entero (int).

## 5. Listas Combinadas
Finalmente, la lista listas contiene las listas cadenas, enteros, flotantes y binarios, lo que demuestra cómo combinar diferentes tipos de datos en una sola lista. print(listas) muestra la lista completa, mientras que print(listas[2]) imprime la lista de flotantes. type(listas) y type(listas[2]) indican que listas es de tipo lista, y el tercer elemento de listas es una lista de flotantes.
