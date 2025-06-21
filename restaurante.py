from mesa import Mesa
from staff import Staff
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
        else:
            return "Empleado no reconocido"
        '''
        elif isinstance(empleado, Mesero):
            return "Mesero"
        elif isinstance(empleado, JefeMesero):
            return "Jefe de Meseros"
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
    
    def Menu(self,empleado,rol):
        if rol == "Staff":
            print("1. Consultar disponibilidad de mesas")
            print("2. Salir")
            opcion = int(input("Ingrese el número de la opción: "))

            if opcion == 1:
                print("\nConsultando disponibilidad de mesas...")
                cantidad_mesa = empleado.consultar_disponibilidad(self.mesas)
                if cantidad_mesa == 0:
                    print("No hay mesas disponibles en el restaurante.")
                else:
                    print(f"Hay {cantidad_mesa} mesas disponibles en el restaurante.")
                
                print("¿Deseas regresar al menú principal? (1: Sí, 2: No)")

                num= int(input("Ingrese su opción: "))
                if num == 1:
                    self.Menu(empleado,rol)
                elif num == 2:
                    print("Saliendo del sistema...")
                    self.iniciar_Sesion()

                else:
                    print("\nOpción no válida, ingrese una opción válida 1 o 2")
                    self.Menu(empleado,rol)

            elif opcion == 2:
                print("Saliendo del sistema...")
                self.iniciar_Sesion()
            else:
                print("\nOpción no válida, ingrese una opción válida 1 o 2")
                self.Menu(empleado,rol)

        else:
            print("Rol no reconocido, no se puede mostrar el menú.")



    def simular(self):
        for i in range(10):
            mesa = Mesa(i)
            if i%2==0:
                mesa.actualizar_estado("No disponible")
            self.mesas.append(mesa)

        miembro = Staff(1, "Andres","1234")
        self.empleados.append(miembro)
              
