from empleado import Empleado

class Mesero(Empleado):
    def __init__(self, id, usuario, contrasena):
        super().__init__(id, usuario, contrasena)
        self.mesas_asignadas = []
        self.mesas_atendidas = []

    def agregar_mesa_asignada(self, mesa):
        if mesa not in self.mesas_asignadas:
            self.mesas_asignadas.append(mesa)
    
    def cantidad_mesas_asignadas(self):
        return len(self.mesas_asignadas)
        
    def mostrar_mesas_asignadas(self):
        if not self.mesas_asignadas:
            print("No tienes mesas asignadas.")
        else:
            c = 1
            for mesa in self.mesas_asignadas:
                print(f"{c}. Mesa {mesa.id}")
                c += 1

    def mostrar_mesas_atendidas(self):
        if not self.mesas_atendidas:
            print("No has atendido mesas.")
        else:
            c = 1
            for mesa in self.mesas_atendidas:
                print(f"{c}. Mesa {mesa.id}")
                c += 1
    
    def ordenar_mesas_por_prioridad(self):
        return sorted([mesa for mesa in self.mesas_asignadas if mesa.estado != "atención"],key=lambda m: m.hora_asignacion)
    
    def atender_mesa(self, mesa):
        if mesa in self.mesas_asignadas:
            mesa.actualizar_estado("atención")
            self.mesas_atendidas.append(mesa) # Agregarla a las mesas atendidas
            self.mesas_asignadas.remove(mesa) # Eliminarla de las mesas asignadas
            print(f"Mesa {mesa.id} está siendo atendida por {self.usuario}.")
        else:
            print(f"Mesa {mesa.id} no está asignada a {self.usuario}.")