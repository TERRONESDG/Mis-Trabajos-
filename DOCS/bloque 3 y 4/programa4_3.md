# Programa 4_3
Uso de la función `range()` y ciclo `for`
# Explicación del programa
La función `range()` se utiliza para generar una secuencia de números. Se puede usar con uno, dos o tres parámetros para especificar el inicio, el final y el paso de la secuencia.

## Ejemplo 1: Imprimir los números del 0 al 9

### Código:

```python
x = range(10)
for num in x:
    print(num)
```
# Tabla de iteración
| Iteración | Valor de `num` |
|-----------|----------------|
|     1     |       0        |
|     2     |       1        |
|     3     |       2        |
|     4     |       3        |
|     5     |       4        |
|     6     |       5        |
|     7     |       6        |
|     8     |       7        |
|     9     |       8        |
|    10     |       9        |


**Explicación:**
- La función `range(10)` genera una secuencia de números del 0 al 9. El número final, 10, no se incluye en la secuencia.
- El ciclo `for` recorre esta secuencia e imprime cada número.

**Resultado:**
```
0
1
2
3
4
5
6
7
8
9
```

---

## Ejemplo 2: Imprimir los números del 5 al 15

### Código:

```python
print("\n Imprime los valores del 5 al 15")  
x1 = range(5, 16)  
for num in x1:
    print(num)
```
# Tabla de iteración
| Iteración | Valor de `num` |
|-----------|----------------|
|     1     |       5        |
|     2     |       6        |
|     3     |       7        |
|     4     |       8        |
|     5     |       9        |
|     6     |      10        |
|     7     |      11        |
|     8     |      12        |
|     9     |      13        |
|    10     |      14        |
|    11     |      15        |

**Explicación:**
- La función `range(5, 16)` genera una secuencia de números que comienza en 5 y termina en 15. El 16 no se incluye en la secuencia.
- El ciclo `for` recorre esta secuencia e imprime los números del 5 al 15.

**Resultado:**
```
5
6
7
8
9
10
11
12
13
14
15
```

---

## Ejemplo 3: Imprimir los números pares del 10 al 20

### Código:

```python
print("\n Imprime los pares del 10 al 20")  
x2 = range(10, 21, 2)  
for num in x2:
    print(num)
```
# Tabla de iteración
| Iteración | Valor de `num` |
|-----------|----------------|
|     1     |      10        |
|     2     |      12        |
|     3     |      14        |
|     4     |      16        |
|     5     |      18        |
|     6     |      20        |

**Explicación:**
- La función `range(10, 21, 2)` genera una secuencia de números que empieza en 10, termina en 20 (el 21 no se incluye), y avanza de dos en dos (por lo tanto, imprime solo los números pares).
- El ciclo `for` recorre esta secuencia e imprime los números pares entre 10 y 20.

**Resultado:**
```
10
12
14
16
18
20
```

---

## Ejemplo 4: Imprimir los números impares del 11 al 21

### Código:

```python
print("\n Imprime los impares del 11 al 21")  
x3 = range(11, 22, 2)  
for num in x3:
    print(num)
```
# Tabla de Iteración
| Iteración | Valor de `num` |
|-----------|----------------|
|     1     |      11        |
|     2     |      13        |
|     3     |      15        |
|     4     |      17        |
|     5     |      19        |
|     6     |      21        |

**Explicación:**
- La función `range(11, 22, 2)` genera una secuencia de números que empieza en 11, termina en 21 (el 22 no se incluye), y avanza de dos en dos, lo que da como resultado solo los números impares.
- El ciclo `for` recorre esta secuencia e imprime los números impares entre 11 y 21.

**Resultado:**
```
11
13
15
17
19
21
```

---

### Resumen de `range()`:
- `range(stop)`: Genera números desde 0 hasta `stop-1`.
- `range(start, stop)`: Genera números desde `start` hasta `stop-1`.
- `range(start, stop, step)`: Genera números desde `start` hasta `stop-1`, avanzando de `step` en `step`.

La función `range()` es muy útil cuando necesitas crear una secuencia de números para iterar en un ciclo `for`. Te permite personalizar el inicio, el final y el paso de la secuencia, lo que te da mucha flexibilidad para trabajar con secuencias de números.
