'''Ejercicio 3. Función encontrar_duplicado : Descripción del ejercicio:
Descripción:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.'''

def encontrar_duplicado(lista):
    set_elementos = set()
    for i in lista:
        if i in set_elementos:
            return i
        else:
            set_elementos.add(i)
    return None

numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(encontrar_duplicado(numeros1))
print(encontrar_duplicado(numeros2))
