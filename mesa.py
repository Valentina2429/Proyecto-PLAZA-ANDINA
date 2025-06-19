class Mesa:
    def __init__(self, id):
        self.id = id
        self.estado = "disponible"
    
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado