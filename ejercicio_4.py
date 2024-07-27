'''
Ejercicio 4. Función enmascarado_datos : Descripción del ejercicio:
Descripción:
Crea una función que convierta una variable en una cadena de texto y 
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
'''

def enmascarado_datos(cadena):
    cadena=str(cadena)
    return '#'*(len(cadena)-4) + cadena[-4:]
