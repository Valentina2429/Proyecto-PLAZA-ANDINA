from empleado import Empleado

class JefeMesero(Empleado):
    def __init__(self, id, usuario, contrasena):
        super().__init__(id, usuario, contrasena)
    
    def consultar_disponibilidad_especifica(self, mesas):
        mesas_disponibles = [mesa for mesa in mesas if mesa.estado == "disponible"]
        if mesas_disponibles:
            print("Mesas disponibles:")
            for mesa in mesas_disponibles:
                print(f"Mesa ID: {mesa.id}, Estado: {mesa.estado}")
        else:
            print("No hay mesas disponibles en el restaurante.")
        return len(mesas_disponibles)