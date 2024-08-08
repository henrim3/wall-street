import numpy as np
from stock_market.stock import Stock
from player import Player


class Transaction:
    def __init__(self, player: Player = None, stock: Stock= None, quantity: int = 0, price: float = 0, buying : bool = False):
        self.player = player
        self.stock = stock
        self.quantity = quantity
        self.price = price  
        self.buying = buying

