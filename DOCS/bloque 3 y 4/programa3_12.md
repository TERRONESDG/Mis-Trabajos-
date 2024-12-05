# Programa 3_12
Método `.pop()` en Listas
# Explicación del programa #
El método `.pop()` se utiliza en Python para eliminar un elemento de una lista en una posición específica o, si no se especifica el índice, elimina el último elemento de la lista. El valor eliminado se devuelve, lo que te permite usarlo si lo necesitas.

## Ejemplo de Uso del Método `.pop()`:

### Código:

```python
nombres = ['andrea', 'marifer', 'adan', 'lucero', 'nena']

# Eliminar el último elemento (sin pasar un índice)
elemento_eliminado = nombres.pop()  # Elimina el último elemento de la lista.
print("Elemento eliminado:", elemento_eliminado)  # Imprime el valor del elemento eliminado.
print("\nLista después de eliminar el último elemento:", nombres)  # Imprime la lista actualizada después de la eliminación.
```

**Explicación:**
- La lista `nombres` inicialmente contiene cinco elementos: `['andrea', 'marifer', 'adan', 'lucero', 'nena']`.
- Al llamar a `nombres.pop()`, el último elemento de la lista, que es `"nena"`, se elimina y se asigna a la variable `elemento_eliminado`.
- Después de esta operación, la lista `nombres` queda como `['andrea', 'marifer', 'adan', 'lucero']`.

```python
# Eliminar un elemento en un índice específico (por ejemplo, índice 2)
elemento_eliminado = nombres.pop(2)  # Elimina el elemento en el índice 2 de la lista.
print("Elemento eliminado en el índice 2:", elemento_eliminado)  # Imprime el valor del elemento eliminado en el índice 2.
print("\nLista después de eliminar el elemento en el índice 2:", nombres)  # Imprime la lista actualizada después de la eliminación.
```

**Explicación:**
- Ahora, la lista `nombres` contiene `['andrea', 'marifer', 'adan', 'lucero']`.
- Al llamar a `nombres.pop(2)`, se elimina el elemento en el índice `2`, que es `"adan"`.
- El valor `"adan"` se elimina de la lista, y la lista `nombres` se actualiza a `['andrea', 'marifer', 'lucero']`.

## Resumen:
- Si no se pasa un índice, `.pop()` elimina y devuelve el último elemento de la lista.
- Si se pasa un índice como argumento (por ejemplo, `nombres.pop(2)`), el método elimina y devuelve el elemento en esa posición específica de la lista.
- El valor eliminado se puede almacenar en una variable si es necesario utilizarlo más tarde.

