import random

class Stock:
    def __init__(self, name="", symbol="", price=0, risklvl=0, potreturn=0, marketinf=0):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.risklvl = risklvl
        self.potreturn = potreturn
        self.marketinf = marketinf
    
    def fluctuate(self):
    # add fluctuate algorithm
        return