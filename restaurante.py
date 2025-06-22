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


                else:
                    print("\nOpción no válida, ingrese una opción válida 1 o 2")
                    self.Menu(empleado,rol)

            elif opcion == 2:
                print("Saliendo del sistema...")

            else:
                print("\nOpción no válida, ingrese una opción válida 1 o 2")
                self.Menu(empleado,rol)
                
        elif rol == "JefeMesero":
            print("1. Consultar mesas disponibles")
            print("2. Asignar mesa y mesero")
            print("3. Salir")
            opcion = int(input("\nIngrese el número de la opción: "))
            if opcion == 1:
                print("\nConsultando mesas disponibles...")
                lista_mesas_dispo = empleado.consultar_disponibilidad_especifica(self.mesas)
                print(f"Hay {lista_mesas_dispo} mesas disponibles en el restaurante.")
                print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
                
                num= int(input("\nIngrese su opción: "))
                if num == 1:
                    self.Menu(empleado,rol)
                elif num == 2:
                    print("Saliendo del sistema...")
            elif opcion ==2:
                mesas_dispo = empleado.consultar_disponibilidad_especifica(self.mesas)
                if not mesas_dispo:
                    print("No hay mesas disponibles.")
                    
            id_mesa = int(input("Ingrese el ID de la mesa: "))
            mesa_elegida = next((m for m in self.mesas if m.id == id_mesa and m.estado == "disponible"), None)
            if not mesa_elegida:
                print("Mesa no valida o no disponible.")
                
            sugerido = empleado.sugerir_mesero()
            if sugerido:
                print(f"Mesero sugerido: {sugerido.usuario} (mesas: {sugerido.contar_mesas_asignadas()})")
                confirm = input("¿Aceptar sugerencia? (s/n): ")
                if confirm != 's':
                    print("Meseros disponibles:")
                    for i, m in enumerate(empleado.meseros):
                        print(f"{i+1}. {m.usuario} ({m.contar_mesas_asignadas()} mesas)")
                    idx = int(input("Seleccione el número del mesero: ")) - 1
                    sugerido = empleado.meseros[idx]

                empleado.asignar_mesa_a_cliente(mesa_elegida)
                empleado.asignar_mesero_a_mesa(mesa_elegida, sugerido)
                print(f" Mesa {mesa_elegida.id} asignada a {sugerido.usuario}")
        
            elif opcion == 3:
                print("Saliendo del sistema...")
                
                
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
        miembro1 = JefeMesero(2, "ValenL","1234")
        self.empleados.append(miembro1)
        miembro2 = Mesero(3, "Santiago", "1234")
        self.mesero.append(miembro2)