from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"
marketsize = 20


class StockMarket:
    def __init__(self):
        self.stocks = []  # {stock_name: price}
        self.stockandtikrs = {}

    def initialize_stocks(self):
        addStocks(self.stocks, self.stockandtikrs, stockfile, marketsize)

    def fluctuate_market(self):
        for stock in self.stocks:
            stock.fluctuate()


    def print_market_status(self, initial):
        if(initial):
            print("Initial Stock Prices:")
        else:
            print("Current Stock Prices:")
        for stock in self.stocks:
            print(f"{stock.tikr}: {stock.name}, ${stock.price:.2f}")
        print("")

    def get_stock(self, tikr):
        return self.stockandtikrs[tikr]
