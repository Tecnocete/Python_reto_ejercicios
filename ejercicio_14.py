'''
Ejercicio 14. No te vayas por las ramas : Explicación del ejercicio:
Descripción: Crea la clase
Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama
e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
Código a seguir:
 Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
 Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
 Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
 Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
 Implementar el método quitar_rama para eliminar una rama en una posición específica.
 Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas 
y las longitudes de las mismas.
Caso de uso:
 Crear un árbol.
 Hacer crecer el tronco del árbol una unidad.
 Añadir una nueva rama al árbol.
 Hacer crecer todas las ramas del árbol una unidad.  Añadir dos nuevas ramas al árbol.
 Retirar la rama situada en la posición 2.
 Obtener información sobre el árbol.
'''

class Arbol():
    def __init__(self):
        self.longitud_tronco = 1
        self.ramas = []
        
    def crecer_tronco(self):
        self.longitud_tronco +=1
    
    def nueva_rama(self):
        self.ramas.append(1)
    
    def crecer_ramas(self):
        self.ramas= [rama + 1 for rama in self.ramas]
        
    def quitar_rama(self,n):
        if n <0 or n > len(self.ramas):
            return "Sigue habiendo las mismas ramas"
        else:
            self.ramas.pop(n)
    
    def info_arbol(self):
        return f"El arbol cuenta con un tronco de {self.longitud_tronco} de longitud, cuenta con {len(self.ramas)} ramas y las ramas tienen las siguientes longitudes {self.ramas}"


# Caso de uso:

arbol1 = Arbol()
arbol1.crecer_tronco()


arbol1.nueva_rama()


arbol1.crecer_ramas()


arbol1.nueva_rama()


arbol1.nueva_rama()

arbol1.quitar_rama(2)

print(arbol1.info_arbol())