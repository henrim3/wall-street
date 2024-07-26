from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"
marketsize = 20
marketshares = 100000


class StockMarket:
    BLUE = "\033[94m"
    END_COLOR = "\033[0m"

    def __init__(self):
        self.stocks: list[Stock] = []
        self.stockandtickers = {}

    def initialize_stocks(self):
        addStocks(self.stocks, self.stockandtickers, stockfile, marketsize, marketshares)

    def fluctuate_market(self):
        for stock in self.stocks:
            stock.fluctuate()

    def print_market_status(self, initial, indent: int = 2):
        indent_str = " " * indent
        width = 130
        headers = ["Price ", "Daily Change", " Total Change"]
        formatted_headers = str(headers[0]) + f"|{headers[1].center(14)}|" + f"{headers[2].center(14)}"
        if (initial):
            print("Initial Stock Prices:")
        else:
            s = (f"Current Stock Prices:")
            padding = width - len(s) - len(formatted_headers)
            pad = " "*padding
            print(f"{s}{pad}{formatted_headers}")
        reachedblue = False
        reachedpenny = False
        for stock in self.stocks:
            if not stock.isbluechip and not reachedpenny:
                headers = [" ", " ", " "]
                formatted_headers = str(headers[0]) + f"|{headers[1].center(14)}|" + f"{headers[2].center(14)}"
                s = (f"{indent_str}Penny Stocks:")
                padding = width - len(s) - len(formatted_headers)
                pad = " "*padding
                print(f"{s}{pad}{formatted_headers}")
                reachedpenny = True
            elif stock.isbluechip and not reachedblue:
                headers = [" ", " ", " "]
                formatted_headers = str(headers[0]) + f"|{headers[1].center(14)}|" + f"{headers[2].center(14)}"
                s = (f"{indent_str}Blue Chip Stocks:")
                padding = width - len(s) - len(formatted_headers)
                pad = " "*padding
                print(f"{s}{pad}{formatted_headers}")
                reachedblue = True
            change = f"{stock.change:.2f}%"
            totchange = f"{stock.totchange:.2f}%"
            if stock.change > 0:
                change = f"+{stock.change:.2f}%"
            if stock.totchange > 0:
                totchange = f"+{stock.totchange:.2f}%"
            s = (f"{indent_str}{indent_str}{stock.ticker}: {stock.name}")
            headers = [f"${stock.price:.2f} ", change, totchange]
            formatted_headers = str(headers[0]) + f"|{headers[1].center(14)}|" + f" {headers[2].ljust(13)}"
            padding = width - len(s) - len(formatted_headers)
            pad = " "*padding
            print(f"{s}{pad}{formatted_headers}")    
        print("")

    def get_stock(self, ticker)-> Stock: 
        return self.stockandtickers.get(ticker)
        
