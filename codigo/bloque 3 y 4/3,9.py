#Programa.9 Igualdad en listas
#Elaborado el 31/10/2024
#Elaborado por : Andrea Guadalupe Jimenez Cardenas

puntos = [10,30,20]
puntos_2 = [10,30,20]
ordenados = [10,20,30]
puntos_textos = ["10","20","30"]

print(puntos==puntos_2) #imprime la comparación y da TRUE
print(puntos==ordenados) #imprime la comparacion y da FALSE
print(puntos=="puntos_textos") #imprime la comparacion y da FALSE
print("\n")

print(puntos!=puntos_2) #imprime la comparación y da FALSE
print(puntos!=ordenados) #imprime la comparación y da TRUE
print(puntos!=puntos_textos) #imprime la comparación y da TRUE