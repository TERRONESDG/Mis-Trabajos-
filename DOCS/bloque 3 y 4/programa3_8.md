# Programa 3_8
Indexing y Subscripting en Listas
# Explicación del programa
### Indexing

En Python, el *indexing* se refiere a acceder a un solo elemento de una lista utilizando su índice. Los índices comienzan desde 0. Aquí mostramos cómo acceder a los elementos de la lista `numeros` utilizando índices positivos y negativos.

```python
print("Indexing")
numeros = [10, 20, 30]
print(numeros[2])  # Accedemos al tercer elemento de la lista (índice 2)
print(numeros[0])  # Accedemos al primer elemento de la lista (índice 0)
print(numeros[1])  # Accedemos al segundo elemento de la lista (índice 1)
```

En este caso, también mostramos cómo usar índices negativos, que permiten acceder a los elementos de la lista comenzando desde el final.

```python
print(numeros[-1])  # Accedemos al último elemento de la lista (índice -1)
```

### Subscripting

El *subscript* (subíndice) se refiere a la acción de seleccionar un rango de elementos de una lista, utilizando una sintaxis de tipo `[start:end]`, donde `start` es el índice de inicio y `end` es el índice de finalización (sin incluir este último). Si se omite el valor de `start`, se asume desde el inicio, y si se omite el valor de `end`, se toma hasta el final de la lista.

```python
print("\nSubscripting")
nombres = ["Chorchis", "Choto", "Emiliano", "Pepe el toro"]
print(nombres[1:])  # Accedemos a los elementos desde el segundo hasta el final
print(nombres[1:5])  # Accedemos a los elementos desde el segundo hasta el quinto (sin incluir el 5)
print(nombres[-2:])  # Accedemos a los dos últimos elementos de la lista (de derecha a izquierda)
```
