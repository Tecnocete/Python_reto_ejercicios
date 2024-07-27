import time

'''
Ejercicio 7. Función fibonacci : Descripción del ejercicio:
Descripción:
Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión.
Definición de la secuencia de Fibonacci:
La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores, 
comenzando con 0 y 1. La posición 0 es la primera:
Ejemplo para los primeros 5 términos de la función de Fibonacci: 0, 1, 1, 2, 3
Primer término: 0 0
 Segundo término: 1 1 
Tercer término: 1 0  1 
Cuarto término: 2 1  1 
Quinto término: 3 1  2
'''
def fibonnaci(n):
    if n<=1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
start_1 = time.time()

fibonnaci(10)       
end_1= time.time()

total_time_1 = end_1-start_1
'''otra opcion bastante más eficiente'''
start_2 = time.time()
def fibonnaci_2(n):
    if n<=1:
        return n 
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b
    
fibonnaci_2(35)

end_2= time.time() 

total_time_2= end_2-start_2 

print(total_time_1)#output 1.624035120010376
print(total_time_2)#output 1.9073486328125e-05
print(total_time_1/total_time_2) #output 85146.2125 es todo esto más rápido con el numero 35 por tanto nos quedamos con la segunda versión. 
