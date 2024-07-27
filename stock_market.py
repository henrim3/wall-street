from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"
marketsize = 20


class StockMarket:
    def __init__(self):
        self.stocks: list[Stock] = []
        self.stockandtickers = {}

    def initialize_stocks(self):
        addStocks(self.stocks, self.stockandtickers, stockfile, marketsize)

    def fluctuate_market(self):
        for stock in self.stocks:
            stock.fluctuate()

    def print_market_status(self, initial):
        if (initial):
            print("Initial Stock Prices:")
        else:
            print("Current Stock Prices:")
        for stock in self.stocks:
            print(f"{stock.ticker}: {stock.name}, ${stock.price:.2f}")
        print("")

    def get_stock(self, ticker):
        if (ticker in self.stockandtickers.keys()):
            return self.stockandtickers[ticker]
        return None

    def get_stocks(self):
        return self.stockandtickers
