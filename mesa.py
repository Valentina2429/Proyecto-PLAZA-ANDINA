class Mesa:
    def __init__(self, id):
        self.id = id
        self.estado = "disponible"
        self.mesero_asignado = None
    
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def asignar_mesero(self, mesero):
        self.asignar_mesero = mesero