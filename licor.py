from producto import Producto
class Licor(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        