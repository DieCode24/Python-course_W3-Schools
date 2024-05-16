# Importación del módulo sys, que proporciona acceso a variables y funciones mantenidas o controladas por el intérprete de Python.
import sys

# Comprobación condicional: Si 5 es mayor que 2.
if 5 > 2:
    # Si la condición es verdadera, se imprime el mensaje "Five is greater than two!".
    print("Five is greater than two!")
    
# Asignación del valor 5 a la variable x.
x = 5
# Asignación del string "Hello, World!" a la variable y.
y = "\n\nHello, World!"

# Impresión de la concatenación del string "Hello, World!" con el string "\nNumber => " y el valor de la variable x convertido a string.
print(y + "\nNumber => " + str(x))