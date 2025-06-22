from empleado import Empleado

class Mesero(Empleado):
    def _init_(self, id, usuario, contrasena):
        super._init_(id, usuario, contrasena)
        
    def mostrar_mesas_asignadas(self):
        if not self.mostrar_mesas_asignadas:
            print("No tienes mesas asignadas.")
            
        else:
            for mesa in self.mostrar_mesas_asignadas:
                print(f"- Mesa {mesa.id}")