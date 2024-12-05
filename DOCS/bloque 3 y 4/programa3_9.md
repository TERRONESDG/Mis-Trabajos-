# programa 3_9
Comparación de Igualdad y Desigualdad en Listas
# Explicación del programa
# Comparación de Igualdad y Desigualdad en Listas

En Python, las listas pueden ser comparadas entre sí utilizando los operadores `==` (igualdad) y `!=` (desigualdad). Estos operadores permiten verificar si las listas son "equivalentes" en contenido y estructura. La comparación no se basa solo en los valores de los elementos, sino también en su orden.

## Comparaciones de Igualdad (`==`)

El operador `==` compara dos listas y devuelve `True` solo si ambas listas tienen exactamente los mismos elementos en el mismo orden. La comparación es **sensible al orden** y **al tipo de los elementos**. Es decir, las listas deben contener los mismos valores en la misma secuencia.

### Ejemplo:
```python
puntos = [10, 30, 20]
puntos_2 = [10, 30, 20]
ordenados = [10, 20, 30]
puntos_textos = ["10", "20", "30"]

print(puntos == puntos_2)  # Compara las listas puntos y puntos_2. Devuelve True porque ambas listas tienen los mismos elementos (10, 30, 20) en el mismo orden.
```

**Explicación:**
- Las listas `puntos` y `puntos_2` tienen los mismos elementos en el mismo orden, por lo que la comparación con `==` devuelve `True`.
- Aunque el contenido sea el mismo, es importante notar que el orden de los elementos sí afecta la comparación, como se muestra a continuación.

```python
print(puntos == ordenados)  # Compara las listas puntos y ordenados. Devuelve False porque el orden de los elementos es diferente.
```

**Explicación:**
- La lista `puntos` contiene los elementos en el orden `[10, 30, 20]`, mientras que `ordenados` tiene el orden `[10, 20, 30]`. Aunque ambos conjuntos de elementos son los mismos, el orden es diferente, por lo que la comparación devuelve `False`.

```python
print(puntos == "puntos_textos")  # Compara la lista puntos con la cadena de texto "puntos_textos". Devuelve False porque son tipos diferentes.
```

**Explicación:**
- En este caso, estamos comparando una lista `puntos` con una cadena de texto `"puntos_textos"`. Dado que los tipos son completamente diferentes (lista de enteros frente a una cadena de texto), la comparación devuelve `False`.

## Comparaciones de Desigualdad (`!=`)

El operador `!=` se utiliza para comprobar si dos listas son diferentes. Esto puede ocurrir si:
- Los elementos no son los mismos.
- El orden de los elementos es diferente.
- Los tipos de datos de los elementos son diferentes.

El operador `!=` devolverá `True` si las listas son diferentes en **cualquier aspecto** y `False` si son idénticas.

### Ejemplo:
```python
print(puntos != puntos_2)  # Compara las listas puntos y puntos_2. Devuelve False porque son iguales (tienen los mismos elementos en el mismo orden).
```

**Explicación:**
- Dado que `puntos` y `puntos_2` tienen exactamente los mismos elementos en el mismo orden, la comparación con `!=` devuelve `False`, ya que las listas son idénticas.

```python
print(puntos != ordenados)  # Compara las listas puntos y ordenados. Devuelve True porque el orden de los elementos es diferente.
```

**Explicación:**
- Como en el caso de `==`, las listas `puntos` y `ordenados` tienen los mismos elementos pero en diferente orden. Esto hace que la comparación con `!=` devuelva `True`, ya que las listas no son iguales.

```python
print(puntos != puntos_textos)  # Compara la lista puntos con la lista puntos_textos. Devuelve True porque son de tipos diferentes (números vs. cadenas).
```

**Explicación:**
- Aquí estamos comparando una lista de enteros `puntos` con una lista de cadenas `puntos_textos`. Aunque ambas listas tienen elementos que representan los mismos números, los tipos de los elementos son diferentes: enteros en `puntos` frente a cadenas de texto en `puntos_textos`. Esto provoca que la comparación devuelva `True`, ya que las listas son consideradas diferentes por su tipo de datos.

