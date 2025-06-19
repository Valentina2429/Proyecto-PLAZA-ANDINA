from empleado import Empleado
from mesa import Mesa

class Staff (Empleado):
    def __init__(self, id,usuario, contrasena):
        super().__init__(id,usuario, contrasena)
    
    def consultar_disponibilidad(self, mesas):
        mesas_disponibles = [mesa for mesa in mesas if mesa.estado == "disponible"]
        return len(mesas_disponibles)