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
    
    def sugerir_mesero(self, empleados):  
        #lista con la cantidad de mesas asignadas por cada mesero
        meseros = [empleado for empleado in empleados if isinstance(empleado, Mesero)]
        if not meseros:
            return []
        else:
            min_mesas = min(mesero.cantidad_mesas_asignadas() for mesero in meseros)
            mismo_nivel = [mesero for mesero in meseros if mesero.cantidad_mesas_asignadas() == min_mesas]
            
        return mismo_nivel
                    
                
    def asignar_mesa_a_cliente(self, mesa):  
        mesa.actualizar_estado("ocupada")
        
    def asignar_mesero_a_mesa(self, mesa, mesero):  
        mesa.asignar_mesero(mesero)
        mesero.agregar_mesa_asignada(mesa)