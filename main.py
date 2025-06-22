from restaurante import Restaurante

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
            restaurante.Menu(empleado, rol)
        elif rol == "JefeMesero":
            print(f"\nHas iniciado sesión como {rol}.")
            print(f'¿Que deseas hacer?')
            restaurante.Menu(empleado, rol)

main()