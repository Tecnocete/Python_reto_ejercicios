'''Ejercicio 15. Clase UsuarioBanco : Explicación del ejercicio:
Descripción: Crea la clase
UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario 
y agregar dinero al saldo.
Código a seguir:
 Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
mediante True y False .
 Implementar el método retirar_dinero para retirar dinero del saldo del
usuario. Lanzará un error en caso de no poder hacerse.
 Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
Lanzará un error en caso de no poder hacerse.
 Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
 Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
 Agregar 20 unidades de saldo de "Alicia".
 Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".  Retirar 50 unidades de saldo a "Alicia".'''

class UsuarioBanco():
    def __init__(self, username,saldo, cuenta = False):
        self.username = username
        self.saldo = saldo
        self.cuenta = cuenta
    def retirar_dinero(self, monto):
        if monto>self.saldo:
            raise ValueError ("No es posible retirar más dinero que el que dispone debe agregar saldo")
        else:
            self.saldo -= monto
    def transferir_dinero(self,otra_persona,monto):
        if not otra_persona.cuenta:
            raise ValueError (f'{otra_persona.username} no tiene cuenta')
        if monto>otra_persona.saldo:
            raise ValueError (f"No es posible retirar más dinero que el que dispone {otra_persona.username} debe agregar saldo")
        else:
            otra_persona.saldo -= monto
            self.saldo += monto
            
            
    def agregar_dinero(self,monto):
        self.saldo += monto
    

usuario1 = UsuarioBanco("Alicia", 100, cuenta=True)
usuario2 = UsuarioBanco("Bob", 50, cuenta=True)

usuario1.agregar_dinero(20)
usuario1.transferir_dinero(usuario2,80)
usuario1.retirar_dinero(50)

