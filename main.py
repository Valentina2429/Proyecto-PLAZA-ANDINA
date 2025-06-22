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
                Menu(restaurante,empleado, rol)
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
        print("2. Salir")
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
        elif opcion == 2:
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