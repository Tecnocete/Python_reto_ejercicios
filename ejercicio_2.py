'''
Ejercicio 2. Función calcular_promedio : Descripción del ejercicio:
Descripción:
Crea una función que calcule el promedio de una lista de números.
'''

def cacular_promedio(list):
    '''
    Función que calcula el promedio de una lista de numeros: 
    
    Parametros:
    -list (list): Una lista de numeros 
    
    Retorna:
    -Float: Valor promerio de la lista
    '''
    try:
        return sum(list)/len(list)
    except ZeroDivisionError as e:
        return (f'El error {e} no se puede dividir entre 0')