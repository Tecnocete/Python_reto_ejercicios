
'''
Ejercicio 6. Función buscar_nombre : Descripción del ejercicio:
Descripción:
Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre 
para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado,
de lo contrario, se lanza una excepción.
Caso de uso:
Incorpora los siguientes nombres a la lista y comprueba que la función funciona correctamente: "Jaime", "Silvia" y "Ana".
'''
def buscar_nombre():
    lista=input("Introduce una lista de nombres separados por comas: ").lower()
    lista_sin_espacio = [nombre.strip() for nombre in lista.split(',')]
    nombre_buscado = input("Introduce el nombre que deseas buscar:").lower().strip()
    if nombre_buscado in lista_sin_espacio:
        print (f'Correcto {nombre_buscado} se encuentra en la lista')
    else: 
        raise ValueError(f"El nombre '{nombre_buscado}' no fue encontrado en la lista.")

