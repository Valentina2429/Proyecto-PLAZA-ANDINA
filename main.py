from restaurante import Restaurante
from empleado import Empleado
from staff import Staff
from JefeMesero import JefeMesero
from mesa import Mesa

def Menu(restaurante,empleado,rol):
    if rol == "Staff":
        print("1. Consultar disponibilidad de mesas")
        print("2. Salir")
        opcion = int(input("Ingrese el número de la opción: "))

        if opcion == 1:
            print("\nConsultando disponibilidad de mesas...")
            cantidad_mesa = empleado.consultar_disponibilidad(restaurante.mesas)
            if cantidad_mesa == 0:
                print("No hay mesas disponibles en el restaurante.")
            else:
                print(f"Hay {cantidad_mesa} mesas disponibles en el restaurante.")
                
            print("¿Deseas regresar al menú principal? (1: Sí, 2: No)")

            num= int(input("Ingrese su opción: "))
            if num == 1:
                Menu(restaurante,empleado,rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

            else:
                print("\nOpción no válida, ingrese una opción válida 1 o 2")
                Menu(restaurante,empleado, rol)

        elif opcion == 2:
            print("Saliendo del sistema...")
            main()

        else:
            print("\nOpción no válida, ingrese una opción válida 1 o 2")
            Menu(restaurante,empleado, rol)
                
    elif rol == "JefeMesero":
        print("1. Consultar mesas disponibles")
        print("2. Asignar mesa a cliente y mesero")
        print("3. Salir")
        opcion = int(input("\nIngrese el número de la opción: "))
        if opcion == 1:
            print("\nConsultando mesas disponibles...")
            lista_mesas_dispo = empleado.consultar_disponibilidad_especifica(restaurante.mesas)
            print(f"Hay {lista_mesas_dispo} mesas disponibles en el restaurante.")
            print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
                
            num= int(input("\nIngrese su opción: "))
            if num == 1:
                Menu(restaurante,empleado, rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

        elif opcion ==2:
            mesas_dispo = empleado.consultar_disponibilidad_especifica(restaurante.mesas)
            if not mesas_dispo:
                print("No hay mesas disponibles.")
            else:
                while True:
                    try:
                        id_mesa = int(input("\nIngrese el ID de la mesa: "))
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
                    mesa_elegida = next((m for m in restaurante.mesas if m.id == id_mesa and m.estado == "disponible"),None)
                    if mesa_elegida:
                        break  # Salir del ciclo si la mesa es válida
                    else:
                        print(" Mesa no válida o no disponible. Intente con otro ID.")

                sugeridos = empleado.sugerir_mesero(restaurante.empleados)
                if sugeridos:
                    print("\nMeseros sugeridos:")
                    for mesero in sugeridos:
                        print(f"Mesero sugerido: {mesero.id} (Mesas asignadas: {mesero.cantidad_mesas_asignadas()})")
                    
                    while True:
                        try:
                            idx = int(input("\nIngrese el número del ID del mesero que desea asignar: ")) 
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue

                        elegido = next((mesero for mesero in sugeridos if mesero.id == idx), None)

                        if elegido:
                            break  
                        else:
                            print(" Mesero no válido o no disponible. Intente con otro ID.")
                
                    empleado.asignar_mesa_a_cliente(mesa_elegida)
                    empleado.asignar_mesero_a_mesa(mesa_elegida, elegido)
                    print(f"\nMesa {mesa_elegida.id} asignada a {elegido.usuario} con ID {elegido.id}.")
                    print("Asignación guardada exitosamente.")

                    print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
                
                    num= int(input("\nIngrese su opción: "))
                    if num == 1:
                        Menu(restaurante,empleado, rol)
                    elif num == 2:
                        print("Saliendo del sistema...")
                        main()

                else:
                    print("No hay meseros disponibles para asignar a la mesa.")

        elif opcion == 3:
            print("Saliendo del sistema...")
            main()
                
        else:
            print("\nOpción no válida, ingrese una opción válida 1 o 2")
            Menu(restaurante,empleado, rol)
                    
    else:
        print("Rol no reconocido, no se puede mostrar el menú.")




def main():
    #Crear instancia del restaurante
    print("\nBienvenido al Restaurante Plaza Andina-Sede Pitalito")
    # falta serializar el restaurante y sus componentes
    restaurante = Restaurante("Plaza Andina-Sede Pitalito")
    restaurante.simular()

    #Iniciar sesion

    empleado = restaurante.iniciar_Sesion()
    if empleado == None:
        print("Usuario o contraseña incorrectos. Saliendo del sistema.")
        main()
    else:
        print(f"\nBienvenido {empleado.usuario} al restaurante {restaurante.nombre}")
        rol = restaurante.verficar_Empleado(empleado)
        
        if rol == "Staff":
            print(f"\nHas iniciado sesión como {rol}.")
            print(f'¿Que deseas hacer?')
            Menu(restaurante,empleado, rol)
        elif rol == "JefeMesero":
            print(f"\nHas iniciado sesión como {rol}.")
            print(f'¿Que deseas hacer?')
            Menu(restaurante,empleado, rol)

main()