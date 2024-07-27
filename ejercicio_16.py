'''Ejercicio 16. Función procesar_texto : Explicación del ejercicio:
 
RETOTEST PYTHON ENUNCIADOS 6
Descripción:
Crea una función llamada
procesar_texto que procesa un texto según la opción especificada:
contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que 
definir primero y llamar dentro de la función
procesar_texto . Código a seguir:
 Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. 
Tiene que devolver un diccionario.
 Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . 
Tiene que devolver el texto con el remplazo de palabras.
 Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.

 Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número 
de argumentos variable según la opción indicada.
Caso de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
Dado el texto de ejemplo, llama a la función procesar_texto para probar sus funcionalidades:
Cuenta el número de veces que aparece cada palabra. Reemplaza la palabra texto por relato.
Elimina la palabra ejemplo.'''

def contar_palabras(texto):
    contador = {}
    texto = texto.lower().split()
    for palabra in texto:
        contador[palabra] = contador.get(palabra,0)+1
    return contador

def reemplazar_palabras(texto,palabra_original,palabra_nueva):
    texto = texto.lower().split()
    lista_definitiva =  []
    for palabra in texto:
        if palabra == palabra_original.lower():
            lista_definitiva.append(palabra_nueva)
        else:
            lista_definitiva.append(palabra)
    return ' '.join(lista_definitiva)

def eliminar_palabras(texto,palabra_a_eliminar):
    texto = texto.lower().split()
    texto_flitrado = [palabra for palabra in texto if palabra != palabra_a_eliminar]
    return ' '.join(texto_flitrado)
  
# Otra manera que se me ha ocurrido tras darle varias vueltas:

def eliminar_palabras_2(texto, palabra_a_eliminar):
    texto = texto.lower().split()
    indices_a_eliminar = [i for i, palabra in enumerate(texto) if palabra == palabra_a_eliminar]
    for i in sorted(indices_a_eliminar, reverse=True):
        texto.pop(i)
    return ' '.join(texto)  

def  procesar_texto(texto,opcion,*args):
    """
    Función que procesa un texto según la opción especificada.
    
    Parámetros:
    - texto (str): El texto que se va a procesar.
    - opcion (str): La opción de procesamiento ("contar", "remplazar" o "eliminar").
    - *args: Argumentos adicionales dependiendo de la opción.
    
    Retorna:
    - Dependiendo de la opción:
        - Si la opción es "contar", retorna un diccionario con el conteo de palabras.
        - Si la opción es "remplazar", retorna el texto con la palabra original reemplazada por la nueva.
        - Si la opción es "eliminar", retorna el texto con la palabra especificada eliminada.
    
    Levanta:
    - ValueError: Si la opción proporcionada no es válida o si el número de argumentos es incorrecto.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "remplazar":
        if len(args) != 2:
            raise ValueError(f"Se esperan dos argumentos para reemplazar. Argumentos pasados: {len(args)}")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError(f"Se espera un argumento para eliminar. Argumentos pasados: {len(args)}")
        return eliminar_palabras(texto, args[0])
    else:
        raise ValueError(f"Opción no válida")
texto = "Este es un ejemplo de texto . Este texto contiene palabras repetidas."
conteo_palabras = procesar_texto(texto, "contar")
print("Conteo de palabras en el texto:")
print(conteo_palabras)

texto_reemplazado = procesar_texto(texto, "remplazar", "texto", "relato")
print("\nTexto con la palabra 'texto' reemplazada por 'relato':")
print(texto_reemplazado)

texto_sin_palabra = procesar_texto(texto, "eliminar", "ejemplo")
print("\nTexto con la palabra 'ejemplo' eliminada:")
print(texto_sin_palabra)
