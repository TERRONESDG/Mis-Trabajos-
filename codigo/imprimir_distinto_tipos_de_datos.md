# imprimir_distinto_tipos_de_datos.md
``` python
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
