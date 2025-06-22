from mesa import Mesa
from staff import Staff
from JefeMesero import JefeMesero
from mesero import Mesero

class Restaurante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mesas = []
        self.empleados = []

    
    def iniciar_Sesion(self):
        print("\nIniciar sesión en el sistema del restaurante")
        usuario = input("\nIngrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        for empleado in self.empleados:
            if empleado.usuario == usuario and empleado.contrasena == contrasena:
                return empleado
        return None
    
    def verficar_Empleado(self, empleado):
        if isinstance(empleado, Staff):
            return "Staff"
        elif isinstance(empleado, JefeMesero):
            return "JefeMesero"
        elif isinstance(empleado, Mesero):
            return "Mesero"
        else:
            return "Empleado no reconocido"

        
        '''
        elif isinstance(empleado, Mesero):
            return "Mesero"

        elif isinstance(empleado, Encargado_barra):
            return "Encargado de Barra"
        elif isinstance(empleado, Jefe_cocina):
            return "Jefe de Cocina"
        elif isinstance(empleado, Auxiliar_cocina):
            return "Auxiliar de Cocina"
        elif isinstance(empleado, Coctelero):
            return "Coctelero"
        elif isinstance(empleado, Cajero):
            return "Cajero"
        '''
    

    def simular(self):
        for i in range(10):
            mesa = Mesa(i)
            if i%2==0:
                mesa.actualizar_estado("No disponible")
            self.mesas.append(mesa)

        miembro = Staff(4, "Andres","1234")
        self.empleados.append(miembro)
        miembro1 = JefeMesero(3, "ValeL","1234")
        self.empleados.append(miembro1)

        miembro3 = Mesero(1, "ValeM","1234")
        self.empleados.append(miembro3)
        miembro1.asignar_mesero_a_mesa(self.mesas[0], miembro3)

        miembro4 = Mesero(2, "Santi","1234")
        self.empleados.append(miembro4)
        miembro1.asignar_mesero_a_mesa(self.mesas[2], miembro4)

        
