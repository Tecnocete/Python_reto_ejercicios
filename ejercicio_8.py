'''
Ejercicio 8. Función encontrar_puesto_empleado : Descripción del ejercicio:
Descripción:
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
Caso de uso:
empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"}, {'nombre': "Mabel", 'apellido': "García",
'puesto': "Product Manager"}, {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]
'''
def encontrar_puesto_empleado (nombre_completo,lista):
    try:
        nombre,apellido = nombre_completo.split()
        for empleado in lista:
            if empleado['nombre'] == nombre and empleado['apellido']==apellido:
                return empleado['puesto'] 
        return(f'{nombre_completo} no trabaja aquí')
    except:
        return('algo va mal')

empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"}, 
             {'nombre': "Mabel", 'apellido': "García",'puesto': "Product Manager"}, 
             {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

print(encontrar_puesto_empleado('Mabel García',empleados))
print(encontrar_puesto_empleado('Juan García',empleados)) 
