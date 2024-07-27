'''

Ejercicio 13. Función sumar_listas usando lambdas: Descripción del ejercicio:
Descripción: Crea una función
lambda que sume elementos correspondientes de dos listas dadas.
Caso de uso:
lista_numeros_1  1, 4, 5, 6 , 7 , 7 ; lista_numeros_2  3, 11, 34, 56
'''
lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]

listas_sumadas = lambda lista_1,lista_2: [x+y for x,y in zip(lista_1,lista_2)] 