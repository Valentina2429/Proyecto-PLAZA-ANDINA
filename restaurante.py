from mesa import Mesa
from staff import Staff
class Restaurante:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mesas = []
        self.meseros = []
        self.staff =[]
        

    def simular(self):
        for i in range(10):
            mesa = Mesa(i)
            if i%2==0:
                mesa.actualizar_estado("No disponible")
            self.mesas.append(mesa)

        miembro = Staff(1, "Andres","1234")
        self.staff.append(miembro)
              
