from restaurante import Restaurante
from empleado import Empleado
from staff import Staff
from JefeMesero import JefeMesero
from mesa import Mesa

def MenuInicio(restaurante,empleado,rol):
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
                MenuInicio(restaurante,empleado,rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

            else:
                print("\nOpción no válida, ingrese una opción válida 1 o 2")
                MenuInicio(restaurante,empleado, rol)

        elif opcion == 2:
            print("Saliendo del sistema...")
            main()

        else:
            print("\nOpción no válida, ingrese una opción válida 1 o 2")
            MenuInicio(restaurante,empleado, rol)
                
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
                MenuInicio(restaurante,empleado, rol)
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
                    
                    print("\n¿Deseas confirmar el pedido? (1: Sí, 2: No ) ")
                    opc = int(input("\nIngrese su occion: "))
                    if opc == 1:
                        print("Asignación guardada exitosamente.")
                    else:
                        print("Saliendo del sistema...")

                    print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No) ")
                
                    num= int(input("\nIngrese su opción: "))
                    if num == 1:
                        MenuInicio(restaurante,empleado, rol)
                    elif num == 2:
                        print("Saliendo del sistema...")
                        main()

                else:
                    print("No hay meseros disponibles para asignar a la mesa.")

        elif opcion == 3:
            print("Saliendo del sistema...")
            main()
                
        else:
            print("\nOpción no válida, ingrese una opción válida 1, 2 o 3")
            MenuInicio(restaurante,empleado, rol)

    elif rol == "Mesero":
        print("1. Consultar orden de mesas asignadas")
        print("2. Notificaciones de atención")
        print("3. Atender una mesa")
        print("4. Mesas atendidas")
        print("5. Salir")
        opcion = int(input("\nIngrese el número de la opción: "))

        # Criterio 2: Orden de atención
        if opcion == 1:
            print("\nConsultando orden de atención...")
            mesasOrdenadas = empleado.ordenar_mesas_por_prioridad()
            if not mesasOrdenadas:
                print("No tienes mesas asignadas.")
            else:
                print(f"\nTienes {len(mesasOrdenadas)} mesas asignadas pendientes.")
                for i, mesa in enumerate(mesasOrdenadas, 1):
                    print(f"{i}. Mesa ID: {mesa.id} | Estado: {mesa.estado}")

            print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
            num = int(input("\nIngrese su opción: "))
            if num == 1:
                MenuInicio(restaurante, empleado, rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

        # Criterio 1: Notificación de atención
        elif opcion == 2:
            print("\nNotificaciones de atención:")
            mesas = [mesa for mesa in empleado.mesas_asignadas if mesa.estado == "ocupada"]
            if not mesas:
                print("No tienes mesas que requieran atención.")
            else:
                c = 1
                for mesa in mesas:
                    print(f"{c}. Mesa {mesa.id}")
                    c += 1

            print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
            num = int(input("\nIngrese su opción: "))
            if num == 1:
                MenuInicio(restaurante, empleado, rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

        # Criterio 4: Confirmar Atención --- Estado = ocupada, Significa que la mesa no está siendo atendida y tiene cliente
        elif opcion == 3:
            print("\nAtendiendo una mesa...")
            mesasOrdenadas = empleado.ordenar_mesas_por_prioridad()
            if not mesasOrdenadas:
                print("No tienes mesas asignadas.")
            else:
                for i, mesa in enumerate(mesasOrdenadas, 1):
                    print(f"{i}. Mesa ID: {mesa.id} | Estado: {mesa.estado}")
                
                while True:
                    try:
                        id_mesa = int(input("\nIngrese el ID de la mesa que desea atender o (0) para Regresar: "))
                        if id_mesa == 0:
                            print("Regresando al menu principal...")
                            MenuInicio(restaurante, empleado, rol)
                        
                        mesa_elegida = next((m for m in mesasOrdenadas if m.id == id_mesa), None)
                        if mesa_elegida:
                            empleado.atender_mesa(mesa_elegida)
                            print(f"\nMesa {mesa_elegida.id} atendida exitosamente.")

                            # Aqui debe continuar el proceso de atención, para tomar el pedido. 
                            # Por ahora solo se imprime un mensaje de éxito.
                            print(f"Mesa {mesa_elegida.id} está siendo atendida por {empleado.usuario}.")

                        else:
                            print("ID de mesa no válida o ya atendida.")
                    except ValueError:
                        print("Entrada inválida. Intente nuevamente.")

        elif opcion == 4:
            print("\nMesas atendidas:")
            empleado.mostrar_mesas_atendidas()
            print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
            num = int(input("\nIngrese su opción: "))
            if num == 1:
                MenuInicio(restaurante, empleado, rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()

        elif opcion == 5:
            print("Saliendo del sistema...")
            main()

        else:
            print("\nOpción no válida, ingrese una opción válida 1 o 2")
            MenuInicio(restaurante,empleado, rol)

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
            MenuInicio(restaurante,empleado, rol)
        elif rol == "JefeMesero":
            print(f"\nHas iniciado sesión como {rol}.")
            print(f'¿Que deseas hacer?')
            MenuInicio(restaurante,empleado, rol)
        elif rol == "Mesero":
            print(f"\nHas iniciado sesión como {rol}.")
            print(f'¿Que deseas hacer?')
            MenuInicio(restaurante,empleado, rol)

main()