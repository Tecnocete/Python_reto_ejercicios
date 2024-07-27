
'''
Ejercicio 5. Función es_anagrama : Descripción del ejercicio:
Descripción:
Crea una función que determine si dos palabras son anagramas, es decir, si están 
formadas por las mismas letras pero en diferente orden.
'''

def  es_anagrama(palabra_1,palabra_2):
    palabra_1= sorted(palabra_1.replace(' ','').lower())
    palabra_2= sorted(palabra_2.replace(' ','').lower())
    if palabra_1==palabra_2:
        return True
    else:
        return False

palabra1 = "Roma"
palabra2 = "lana"
palabra3 = " hola"
palabra4 = "amor"

print(es_anagrama(palabra1,palabra2))
print(es_anagrama(palabra1,palabra3))
print(es_anagrama(palabra1,palabra4))
print(es_anagrama(palabra2,palabra3))
print(es_anagrama(palabra2,palabra4))
print(es_anagrama(palabra3,palabra4))