from .carta import Carta

class Efecto(Carta):
    def __init__(self, nombre, costo, texto, status, magnitud):
        super().__init__(nombre, costo)
        self.texto= texto
        self.status= status
        self.magnitud=magnitud


    def genera_efecto(self,unidad):  
        if self.status == "Resistencia":
            unidad.modifica_resistencia(self.magnitud)
        else: 
            self.status == "Poder"
            unidad.modifica_poder(self.magnitud)