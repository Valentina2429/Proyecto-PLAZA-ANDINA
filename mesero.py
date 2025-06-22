from empleado import Empleado

class Mesero(Empleado):
    def __init__(self, id, usuario, contrasena):
        super().__init__(id, usuario, contrasena)
        self.mesas_asignadas = []

    def agregar_mesa_asignada(self, mesa):
        if mesa not in self.mesas_asignadas:
            self.mesas_asignadas.append(mesa)
    
    def cantidad_mesas_asignadas(self):
        return len(self.mesas_asignadas)
        
    def mostrar_mesas_asignadas(self):
        if not self.mesas_asignadas:
            print("No tienes mesas asignadas.")
            
        else:
            for mesa in self.mesas_asignadas:
                print(f"- Mesa {mesa.id}")