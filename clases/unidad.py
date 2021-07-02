from .carta import Carta

class Unidad(Carta):
    
    def __init__(self, nombre, costo, resistencia, poder):
        super().__init__(nombre, costo)
        self.resistencia = resistencia
        self.poder = poder

    def modifica_poder(self,num):
        self.poder = self.poder + num

    def modifica_resistencia(self,num):
        self.resistencia = self.resistencia + num

    def ataque(self,unidad):
        unidad.modifica_resistencia(-self.poder)