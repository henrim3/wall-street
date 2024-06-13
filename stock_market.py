from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"


class StockMarket:
    def __init__(self):
        self.stocks = []  # {stock_name: price}
        self.stockandsymbols = {}

    def initialize_stocks(self):
        addStocks(self.stocks, self.stockandsymbols, stockfile)

    def fluctuate_market(self):
        for stock in self.stocks:
            stock.fluctuate()


    def print_market_status(self):
        print("Current Stock Prices:")
        for stock in self.stocks:
            print(f"{stock.symbol}: {stock.name} ${stock.price}")

    def get_stock(self, symbol):
        return self.stockandsymbols[symbol]