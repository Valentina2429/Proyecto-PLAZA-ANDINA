from restaurante import Restaurante
from empleado import Empleado
from staff import Staff
from JefeMesero import JefeMesero
from mesa import Mesa

def MenuInicio(restaurante,empleado,rol):
    if rol == "Staff":
        print("_____________________________________________________________________________________")
        print("\nBienvenido al menú del Staff")
        print("¿Qué deseas hacer?")
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
        print("_____________________________________________________________________________________")
        print("\nBienvenido al menú del Jefe de Meseros")
        print("¿Qué deseas hacer?")
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
                MenuInicio(restaurante, empleado, rol)
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
                    
                    print("\n¿Deseas confirmar la asignacion? (1: Sí, 2: No ) ")
                    opc = int(input("\nIngrese su opcion: "))
                    if opc == 1:
                        print("Asignación guardada exitosamente.")
                    else:
                        print("Regresando al menú principal...")
                        MenuInicio(restaurante, empleado, rol)

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
        print("_____________________________________________________________________________________")
        print("\nBienvenido al menú del Mesero")
        print("¿Qué deseas hacer?")
        print("1. Consultar orden de mesas asignadas")
        print("2. Atender una mesa")
        print("3. Mesas atendidas")
        print("4. Registrar pedido")
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


        # Criterio 4: Confirmar Atención --- Estado = ocupada, Significa que la mesa no está siendo atendida y tiene cliente
        elif opcion == 2:
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

        elif opcion == 3:
        
            print("\nMesas atendidas:")
            empleado.mostrar_mesas_atendidas()
            print("\n¿Deseas regresar al menú principal? (1: Sí, 2: No)")
            num = int(input("\nIngrese su opción: "))
            if num == 1:
                MenuInicio(restaurante, empleado, rol)
            elif num == 2:
                print("Saliendo del sistema...")
                main()
        
        #Funcionalidad 5 para registrar un pedido
        elif opcion == 4:
            pedido =[]
            while True:
                try:
                    print("\n¿Que deseas hacer?")
                    print("1. Agregar producto al pedido")
                    print("2. Modificar cantidad de productos del pedido")
                    print("3. Eliminar productos del pedido")
                    print("4. Modificar obervaciones")
                    print("5. Previsulizar pedido y confirmar")
                    print("6. Salir")
                    num = int(input("\nIngrese su opción:"))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue   

                #Agregar producto al pedido
                if num==1:
                    while True:
                        try:
                            print("\n¿Deseas agregar un nuevo producto al pedido? (1: Sí, 2: No)")
                            eleccion = int(input("Ingrese su opción: "))
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue 

                        if eleccion == 1:
                            print("\nPara registrar pedido...")
                            print("Elige la categoria del producto que deseas registrar:")
                            print("1. Comida")
                            print("2. Licor")
                            print("3. Coctel")      

                            #Criterio 2: Seleccionar categoria del menu  
                            while True:
                                try:
                                    categoria = int(input("Ingrese el número de la de la categoria deseada: "))
                                except ValueError:
                                    print("Por favor, ingrese un número.")
                                    continue
                                if categoria in [1, 2, 3]:
                                    break
                                else:
                                    print("Categoría no válida. Ingrese 1, 2 o 3.")

                            menu_por_categoria = restaurante.menu_por_tipo("Comida" if categoria == 1 else "Licor" if categoria == 2 else "Coctel")


                            #Criterio 3: Seleccionar producto del menu
                            while True:
                                try:
                                    producto = int(input("\nIngresa el numero del producto que deseas agregar al pedido:"))
                                except ValueError:
                                    print("Por favor, ingrese un número.")
                                    continue
                                if producto!=0 and producto<=len(menu_por_categoria):
                                    break
                                else:
                                    print("Categoría no válida.")
                            
                            #Criterio 4:Ingresar la cantidad del producto
                            while True:
                                try:
                                    cantidad = int(input("\nIngresa la cantidad del producto que deseas agregar al pedido:"))
                                except ValueError:
                                    print("Por favor, ingrese un número.")
                                    continue
                                if cantidad>0:
                                    break
                                else:
                                    print("Cantidad no válida. Debe ser un número positivo.")

                            
                            obs = input("\nIngrese una observación para el producto (opcional, sino aplica ponga N/A):")

                            pedido.append((menu_por_categoria[producto-1], cantidad, obs))
                            print(f"\nProducto {menu_por_categoria[producto-1].nombre} ha sido agregado al pedido. Cantidad: {cantidad} con la siguiemte observacion {obs}")


                        elif eleccion == 2:
                            break
                        else:
                            print("Opción no válida. Por favor, ingrese 1 o 2.")
                
                #Criterio 5: Modificar cantidad de productos del pedido
                elif num==2:
                    print("Productos actuales en el pedido:")
                    for i, (prod, cant,obs) in enumerate(pedido,1):
                        print(f"{i}. {prod.nombre} - Cantidad: {cant} - Observación: {obs}")

                    while True:
                        try:
                            modificar = int(input("Ingrese el número del producto que desea modificar (0 para salir): "))
                            if modificar == 0:
                                break
                            elif 1 <= modificar <= len(pedido):
                                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {pedido[modificar-1][0].nombre}: "))
                                if nueva_cantidad > 0:
                                    pedido[modificar-1] = (pedido[modificar-1][0], nueva_cantidad)
                                    print(f"Cantidad de {pedido[modificar-1][0].nombre} actualizada a {nueva_cantidad}.")
                                else:
                                    print("Cantidad no válida. Debe ser un número positivo.")
                            else:
                                print("Número de producto no válido.")
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                
                #Criterio 6: Eliminar productos del pedido
                elif num==3:
                    print("Productos actuales en el pedido:")
                    for i, (prod, cant, obs) in enumerate(pedido, 1):
                        print(f"{i}. {prod.nombre} - Cantidad: {cant} - Observación: {obs}")

                    while True:
                        try:
                            eliminar = int(input("Ingrese el número del producto que desea eliminar (0 para salir): "))
                            if eliminar == 0:
                                break
                            elif 1 <= eliminar <= len(pedido):
                                eliminado = pedido.pop(eliminar-1)
                                print(f"Producto {eliminado[0].nombre} eliminado del pedido.")
                            else:
                                print("Número de producto no válido.")
                        except ValueError:
                            print("Por favor, ingrese un número válido.")

                #Criterio 7: Modificar observaciones
                elif num==4:   
                    print("Productos actuales en el pedido:")
                    for i, (prod, cant, obs) in enumerate(pedido, 1):
                        print(f"{i}. {prod.nombre} - Cantidad: {cant} - Observación: {obs}")

                    while True:
                        try:
                            modificar_obs = int(input("Ingrese el número del producto cuya observación desea modificar (0 para salir): "))
                            if modificar_obs == 0:
                                break
                            elif 1 <= modificar_obs <= len(pedido):
                                nueva_obs = input(f"Ingrese la nueva observación para {pedido[modificar_obs-1][0].nombre}: ")
                                pedido[modificar_obs-1] = (pedido[modificar_obs-1][0], pedido[modificar_obs-1][1], nueva_obs)
                                print(f"Observación de {pedido[modificar_obs-1][0].nombre} actualizada a '{nueva_obs}'.")
                            else:
                                print("Número de producto no válido.")
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                
                #Criterio 8: Previsualizar pedido y confirmar
                elif num==5:
                    
                    if not pedido:
                        print("No hay productos en el pedido.")
                    else:
                        print("\nPedido actual:")
                        total = 0
                        for prod, cant, obs in pedido:
                            subtotal = prod.precio * cant
                            total += subtotal
                            print(f"{prod.nombre} - Cantidad: {cant}- Observaciones: {obs} - Subtotal: ${subtotal:.2f}")
                        print(f"Total del pedido: ${total:.2f}")

                        confirmar = int(input("\n¿Deseas confirmar el pedido? (1:si/2:no): "))
                        if confirmar == 1:
                            print("Pedido confirmado.")
                            empleado.mesas_atendidas[-1].pedido = pedido
                        else:
                            
                            print("Pedido no confirmado. Regresando al menú principal.")

                elif num==6:
                    MenuInicio(restaurante, empleado, rol)

                else:
                    print("Opción no válida. Por favor, ingrese 1, 2, 3 o 4.")
        
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
            MenuInicio(restaurante,empleado, rol)
        elif rol == "JefeMesero":
            print(f"\nHas iniciado sesión como {rol}.")
            MenuInicio(restaurante,empleado, rol)
        elif rol == "Mesero":
            print(f"\nHas iniciado sesión como {rol}.")
            MenuInicio(restaurante,empleado, rol)

main()