class Mesa:
    def __init__(self, id):
        self.id = id
        self.estado = "disponible"
        self.cliente = None
        self.mesero_asignado = None
    
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def set_cliente(self, cliente):
        self.cliente = cliente
    
    def asignar_mesero(self, mesero):
        self.mesero_asignado = mesero