# Programa 4_2
Ciclo `for` para recorrer listas de nombres y frutas
# Explicación del programa 
El ciclo `for` permite recorrer una lista de manera eficiente y realizar una acción sobre cada elemento de la lista, sin necesidad de referirse a los índices. Esto es especialmente útil cuando no sabemos cuántos elementos hay en la lista o cuando la lista puede cambiar.

## Ejemplo 1: Recorrer una lista de nombres

### Código:

```python
nombres = ["luis", "Juan", "Eduardo", "Marcos", "Chuy"]

# Recorrer la lista de nombres e imprimir cada nombre
for nombre in nombres:
    print("El nombre es", nombre)
```

**Explicación:**
- En este código, la lista `nombres` contiene cinco nombres.
- El ciclo `for` recorre cada elemento de la lista, y en cada iteración, la variable `nombre` toma el valor del siguiente elemento de la lista.
- Usamos `print()` para mostrar el valor de `nombre` en cada iteración.

**Resultado:**
```
El nombre es luis
El nombre es Juan
El nombre es Eduardo
El nombre es Marcos
El nombre es Chuy
```
# Tabla de Iteración 

| Iteración | Valor de `nombre`  |
|-----------|--------------------|
|     1     |        luis        |
|     2     |        Juan        |
|     3     |       Eduardo      |
|     4     |       Marcos       |
|     5     |        Chuy        |

---

## Ejemplo 2: Recorrer una lista de frutas

### Código:

```python
# Lista de frutas
frutas = ["Manzana", "Piña", "Platano"]

# Recorrer la lista de frutas e imprimir cada fruta
for fruta in frutas:
    print("La fruta es:", fruta)
```
# Tabla de iteración

| Iteración | Valor de `nombre` |
|-----------|-------------------|
|     1     |       luis        |
|     2     |       Juan        |
|     3     |      Eduardo      |
|     4     |      Marcos       |
|     5     |       Chuy        |


**Explicación:**
- En este caso, la lista `frutas` contiene tres elementos.
- Al igual que en el ejemplo anterior, el ciclo `for` recorre la lista y en cada iteración, la variable `fruta` toma el valor de cada elemento de la lista.
- En cada ciclo, se imprime el nombre de la fruta utilizando `print()`.

**Resultado:**
```
La fruta es: Manzana
La fruta es: Piña
La fruta es: Platano
```
# Tabla de iteración
| Iteración | Valor de `fruta`  |
|-----------|-------------------|
|     1     |     Manzana       |
|     2     |       Piña        |
|     3     |      Platano      |


---

### Ventajas del uso del ciclo `for`:

- **Reutilización**: El ciclo `for` permite ejecutar una misma acción (como imprimir) sin necesidad de escribir repetidamente una instrucción `print()` para cada elemento de la lista.
- **Flexibilidad**: Si la lista cambia o crece, el ciclo `for` continuará funcionando correctamente sin necesidad de modificar el código.
- **Menor código**: Es más eficiente que escribir manualmente un `print()` por cada elemento, lo que hace que el código sea más limpio y fácil de mantener.

Este es un ejemplo simple de cómo el ciclo `for` facilita la iteración a través de una lista y ejecuta una acción para cada uno de los elementos. También ayuda a evitar la repetición de código, lo que mejora la legibilidad y mantenibilidad del programa.
