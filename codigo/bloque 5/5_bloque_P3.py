#programa 3: funciones con listas
#Fecha de elaboraciÓn: 13/11/2024
#Elaborado por : Diego Andres Terrones Gonzalez.

print("Funcion list")
cadena = "Hola"
lista = list(cadena)
print(lista)

print("Funcion len")
cadena2 = "Hola numdo"
longitud = len(cadena2)
print(longitud)

print("Funcion min")
numeros = [1, 2, 3, 4, 5]
resultado = min(numeros)
print(resultado)

print("Funcion max")
numeros2 = [1, 2, 3, 4, 5]
res = max(numeros2)
print(res)

print("Funcion sorted")
numeros3 = [1, 2, 3, 4, 5]
result = sorted(numeros3)
print(result)

print("Funcion reversed")
numeros4 = [1, 2, 3, 4, 5]
result2 = list(reversed(numeros4))
print(result2)

print("Funcion enumerate")
frutas = ["manzana", "banana", "cereza"]
for indice,fruta in enumerate(frutas):
    print(f"indice: {indice}, fruta:{fruta}")

print("Funcion zip")
nombres = ["juan", "maria", "carlos"]
edades = [23, 45, 14]
res2 = zip(nombres,edades)
print(list(res2))

