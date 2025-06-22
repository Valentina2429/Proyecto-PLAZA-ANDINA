from empleado import Empleado
from mesero import Mesero
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
    
    def sugerir_mesero(self, meseros):  
        if not self.meseros:
            return None
        return min(self.meseros, key=lambda m: m.contar_mesas_asignadas())
    
    def asignar_mesa_a_cliente(self, mesa):  
        mesa.actualizar_estado("ocupada")
        
    def asignar_mesero_a_mesa(self, mesa, mesero):  
        mesa.asignar_mesero(mesero)
        mesero.mesas_asignadas.append(mesa)