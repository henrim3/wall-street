import random
import numpy as np # type: ignore

class Stock:
    def __init__(self, name="", tikr="", price=0, risklvl=0, potreturn=0, marketinf=0, mu=0.1, sigma=0.2, dt=1/252):
        self.name = name
        self.tikr = tikr
        self.price = price
        self.risklvl = risklvl
        self.potreturn = potreturn
        self.marketinf = marketinf
        self.change = '\0'
        self.mu = mu        # Drift coefficient
        self.sigma = sigma  # Volatility coefficient
        self.dt = dt        # Time increment
        self.owned = 0
        self.needed = 1000
        self.marketcap = 0.01
    
    def fluctuate(self):
        tmp = self.price
        # Generate a random number from a standard normal distribution
        W = np.random.standard_normal()
        # Update the stock price using GBM formula
        self.price = self.price * np.exp((self.mu - 0.5 * self.sigma**2) * self.dt + self.sigma * np.sqrt(self.dt) * W)
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
