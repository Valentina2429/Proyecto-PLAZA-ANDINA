from mesa import Mesa
from staff import Staff
from JefeMesero import JefeMesero
from mesero import Mesero
from comida import Comida
from licor import Licor
from coctel import Coctel

class Restaurante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mesas = []
        self.empleados = []
        self.menu = []

    
    def iniciar_Sesion(self):
        print("\nIniciar sesión en el sistema del restaurante")
        usuario = input("\nIngrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        for empleado in self.empleados:
            if empleado.usuario == usuario and empleado.contrasena == contrasena:
                return empleado
        return None
    
    def agregar_profucto_menu(self, producto):
        self.menu.append(producto)
    
    def menu_por_tipo(self, tipo):
        print(f"\nMenu de {tipo}:")
        tipo = tipo.capitalize()
        categoria = []
        i=1

        for producto in self.menu:
            if tipo == "Comida" and isinstance(producto, Comida):
                print(f"{i}.{producto.nombre} - ${producto.precio:.2f}")
                categoria.append(producto)
                i+=1

            elif tipo == "Licor" and isinstance(producto, Licor):
                print(f"{i}.{producto.nombre} - ${producto.precio:.2f}")
                categoria.append(producto)
                i+=1

            elif tipo == "Coctel" and isinstance(producto, Coctel):
                print(f"{i}.{producto.nombre} - ${producto.precio:.2f}")
                categoria.append(producto)
                i+=1

        return categoria


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
        # Asignar primero a los clientes
        miembro1.asignar_mesa_a_cliente(self.mesas[1])
        miembro1.asignar_mesa_a_cliente(self.mesas[3])
        miembro1.asignar_mesa_a_cliente(self.mesas[5])

        # Asignar meseros a las mesas
        miembro1.asignar_mesero_a_mesa(self.mesas[1], miembro4)
        miembro1.asignar_mesero_a_mesa(self.mesas[3], miembro4)
        miembro1.asignar_mesero_a_mesa(self.mesas[5], miembro4)

        produ1 = Comida("Hamburguesa", 11000)
        produ2 = Comida("Pizza", 8999)
        produ3 = Licor("Cerveza", 3500)
        produ4 = Coctel("Mojito", 5000)
        produ5 = Comida("Ensalada", 7800)
        produ6 = Licor("Vino", 12000)
        produ7 = Coctel("Piña Colada", 12000)
        produ8 = Comida("Tacos", 9900)
        produ9 = Licor("Tequila", 40000)
        produ10 = Coctel("Daiquiri", 13000)
        

        self.agregar_profucto_menu(produ1)
        self.agregar_profucto_menu(produ2)
        self.agregar_profucto_menu(produ3)
        self.agregar_profucto_menu(produ4)
        self.agregar_profucto_menu(produ5)
        self.agregar_profucto_menu(produ6)
        self.agregar_profucto_menu(produ7)
        self.agregar_profucto_menu(produ8)
        self.agregar_profucto_menu(produ9)
        self.agregar_profucto_menu(produ10)
        