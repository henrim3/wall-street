import random

class Stock:
    def __init__(self, name="", tikr="", price=0, risklvl=0, potreturn=0, marketinf=0):
        self.name = name
        self.tikr = tikr
        self.price = price
        self.risklvl = risklvl
        self.potreturn = potreturn
        self.marketinf = marketinf
        self.change = '\0'
        self.flucval = 1.02
        self.owned = 0
        self.needed = 1000
        self.marketcap = 0.01
    
    def fluctuate(self):
        tmp = self.price
        self.price = self.price * self.flucval
        self.change = self.price - tmp
        self.price = round(float(self.price), 2)
    
    def printinfo(self):
        print(f"\nName: {self.name}")
        print(f"Tikr: {self.tikr}")
        print(f"Price: {self.price:.2f}")
        print(f"Change:{self.change:.2f}")
        print(f"Current shares owned: {self.owned}")
        print(f"Shares needed: {self.needed}")
        print(f"Market cap: {self.marketcap} \n")