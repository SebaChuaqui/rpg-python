from carta import Card

class Unit(Card):
    def __init__(self, nombre, valor, poder, respuesta, resistencia):
        super().__init__(nombre, valor, poder, resistencia)
        self.valor = valor
        self.respuesta = respuesta

    def cinturon_rojo(self, costo, poder, resistencia):
        self.costo = 3
        self.poder = 3
        self.resistencia = 4

    def cinturon_negro(self, costo, poder, resistencia):
        self.costo = 4
        self.poder = 5
        self.resistencia = 4
