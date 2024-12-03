# Programa 2.2
Programa donde si 2 personas van a la fiesta, entonces no hay fiesta
# Explicación del programa.

## Imprimir la negación de las expresiones OR

``print(not(False or False))``   Resultado: True, ya que False or False es False, y 'not' invierte a True

``print(not(False or True))``    Resultado: False, ya que False or True es True, y 'not' invierte a False

``print(not(True or False))``    Resultado: False, ya que True or False es True, y 'not' invierte a False

``print(not(True or True))``     Resultado: False, ya que True or True es True, y 'not' invierte a False

# Explicación de los operadores:
``or`` (Compuerta OR):

La compuerta OR devuelve ``True`` si al menos uno de los dos valores es ``True``. Si ambos son ``False``, el resultado es ``False``.

``False or False``: Da ``False`` porque ambos son ``False``.

``False or True``: Da ``True`` porque uno de los valores es ``True``.

``True or False``: Da ``True`` porque uno de los valores es ``True``.

``True or True``: Da ``True`` porque ambos son ``True``.

``not`` (Negación lógica):

El operador ``not`` invierte el valor lógico de una expresión.

``not(False or False)``: Invierte el valor de ``False``, por lo que da ``True``.

``not(False or True)``: Invierte el valor de ``True``, por lo que da ``False``.

``not(True or False)``: Invierte el valor de ``True``, por lo que da ``False``.

``not(True or True)``: Invierte el valor de ``True``, por lo que da ``False``.
