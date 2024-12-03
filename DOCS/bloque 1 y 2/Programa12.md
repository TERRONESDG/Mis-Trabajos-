# Programa 12
Compuertas OR y AND
# Explicación del programa

## Imprimir el resultado de las compuertas OR
```python
print("Compuertas or")
```

``print(False or False)``   Resultado: False, ya que OR solo es True si al menos uno de los valores es True

``print(False or True)``    Resultado: True, ya que OR devuelve True si uno de los valores es True

``print(True or False)``    Resultado: True, ya que OR devuelve True si uno de los valores es True

``print(True or True)``     Resultado: True, ya que OR devuelve True si al menos uno es True

``print("\n")``  Salto de línea

## Imprimir el resultado de las compuertas AND
```python
print("Compuertas and")
```
``print(False and False)``   Resultado: False, ya que AND solo es True si ambos valores son True

``print(True and False)``    Resultado: False, ya que AND requiere que ambos valores sean True

``print(True and True)``     Resultado: True, ya que AND devuelve True solo si ambos son True

``print("\n")``   Salto de línea

# Explicación de los operadores lógicos:

``or`` (Compuerta OR):

La compuerta OR devuelve ``True`` si al menos uno de los dos valores es ``True``. Si ambos son ``False``, el resultado es ``False``.

``False or False``: Da ``False`` porque ambos valores son ``False``.

``False or True``: Da ``True`` porque uno de los valores es ``True``.

``True or False``: Da ``True`` porque uno de los valores es ``True``.

``True or True``: Da ``True`` porque ambos valores son ``True``.

``and`` (Compuerta AND):

La compuerta AND devuelve ``True`` solo si ambos valores son ``True``. Si uno o ambos son ``False``, el resultado es ``False``.

``False and False``: Da ``False`` porque ambos valores son ``False``.

``True and False``: Da ``False`` porque uno de los valores es ``False``.

``True and True``: Da ``True`` porque ambos valores son ``True``.
