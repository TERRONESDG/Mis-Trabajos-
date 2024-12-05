# Programa 4_1
Ciclo `for` para recorrer una lista
# Explicación del programa
El ciclo `for` es útil cuando necesitamos recorrer todos los elementos de una lista de manera eficiente. En lugar de acceder a cada elemento de la lista mediante su índice, podemos usar `for` para iterar directamente sobre los elementos de la lista.

## Ejemplo con el ciclo `for`:

### Código:

```python
lista_num = [10, 30, 40, 20, 35, 80]

# Imprimiendo cada elemento de la lista manualmente (sin usar for)
print(lista_num[0])
print(lista_num[1])
print(lista_num[2])
print(lista_num[3])
print(lista_num[4])
print(lista_num[5])
```

**Explicación:**
- En este ejemplo, se accede a cada elemento de la lista `lista_num` por su índice. 
- Usamos `print()` para imprimir los valores de la lista manualmente. Esto funciona, pero es tedioso si la lista tiene muchos elementos.

### Código optimizado con ciclo `for`:

```python
# Realizando la misma tarea con un ciclo for
for i in lista_num:
    print(i)
```
## Ejemplo de la iteración

| Iteración | Valor de `i` (Elemento de la lista) |
|-----------|-------------------------------------|
|     1     |                 10                  |
|     2     |                 30                  |
|     3     |                 40                  |
|     4     |                 20                  |
|     5     |                 35                  |
|     6     |                 80                  |


**Explicación:**
- En lugar de acceder a cada elemento de la lista usando su índice, utilizamos un ciclo `for` para recorrer la lista completa.
- La variable `i` toma el valor de cada elemento de la lista en cada iteración del ciclo.
- La instrucción `print(i)` imprime cada elemento de la lista, lo que hace que el código sea más corto y fácil de mantener.

### Resultado:
Ambos fragmentos de código imprimirán lo siguiente:

```
10
30
40
20
35
80
```

**Ventajas del ciclo `for`:**
- Es más corto y limpio, especialmente cuando estamos trabajando con listas grandes.
- El ciclo `for` permite recorrer la lista sin tener que referirse explícitamente al índice de cada elemento, lo que mejora la legibilidad y mantenimiento del código.

