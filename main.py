from restaurante import Restaurante
from empleado import Empleado
from staff import Staff

def main():
    #Crear instancia del restaurante
    print("\nBienvenido al Restaurante Plaza Andina-Sede Pitalito")
    restaurante = Restaurante("Plaza Andina-Sede Pitalito")
    restaurante.simular()
    print("Selecciona tu rol:\n1.Miembro del staff\n2.Jefe de meseros\n3.Mesero")
    opcion =int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        print("Has seleccionado el rol de Miembro del staff.\n")
        usuario = input("Ingrese su ID de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # Verificar si el usuario y contraseña son correctos
        for i in range(len(restaurante.staff)):
            if (usuario, contrasena) == (restaurante.staff[i].usuario, restaurante.staff[i].contrasena):
                print(f"\nBienvenido {restaurante.staff[i].usuario} al restaurante {restaurante.nombre}")
                staff = restaurante.staff[i]

                # Consultar disponibilidad de mesas
                print("¿Que deseas hacer?\n")
                print("1. Consultar disponibilidad de mesas")
                opcion = int(input("Ingrese el número de la opción: "))
                if opcion != 1:
                    print("Opción no válida. Saliendo del sistema.")
                else:
                    print("\nConsultando disponibilidad de mesas...")
                    cantidad_mesa = staff.consultar_disponibilidad(restaurante.mesas)
                    if cantidad_mesa == 0:
                        print("No hay mesas disponibles en el restaurante.")
                    else:
                        print(f"Hay {cantidad_mesa} mesas disponibles en el restaurante.")
                        break
        else:
            print("Usuario o contraseña incorrectos.")

    else:
        print("Aun no estan disponibles las otras opciones")    
print("cambio 1")
main()



