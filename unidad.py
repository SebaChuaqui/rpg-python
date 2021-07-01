from carta import Card

class Unit:
    def __init__(self, nombre, valor, poder, respuesta):
        super().__init__(nombre, valor)
        self.nombre = nombre
        self.valor = valor
        self.poder = poder
        self.respuesta = respuesta

    

