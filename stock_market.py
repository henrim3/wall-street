from stock import Stock
from stockparser import addStocks

stockfile = "data/NASDAQ.txt"
marketsize = 20
marketshares = 100000
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'



class StockMarket:

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
        width = 120
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
            midpadding = 14 - len(change)
            headers = [f"${stock.price:.2f} ", change, totchange]
            if stock.change > 0:
                midpadding -= 1
            if stock.change > 0:
                change = f"+{stock.change:.2f}%"
                coloredchange = f"{GREEN}+{stock.change:.2f}%{RESET}"
            elif stock.change < 0:
                coloredchange = f"{RED}{stock.change:.2f}%{RESET}"
            if stock.totchange > 0:
                change = f"+{stock.totchange:.2f}%"
                coloredtotchange = f"{GREEN}+{stock.totchange:.2f}%{RESET}"
            elif stock.totchange < 0:
                coloredtotchange = f"{RED}{stock.totchange:.2f}%{RESET}"
            s = (f"{indent_str}{indent_str}{stock.ticker}: {stock.name}")
            headers = [f"${stock.price:.2f} ", change, totchange]
            leftpadding = " " * (midpadding // 2 + midpadding % 2)
            rightpadding = " " * (midpadding // 2)
            formatted_headers = headers[0] + f"|" + leftpadding + headers[1] + rightpadding + "|" + f" {headers[2].ljust(13)}"
            padding = width - len(s) - len(formatted_headers)
            pad = " "*padding
            coloredheader = f"{YELLOW}${stock.price:.2f} {RESET}"+ f"|" + leftpadding + coloredchange + rightpadding + "|" + f" {coloredtotchange}"
            print(f"{s}{pad}{coloredheader}")    
        print("")

    def get_stock(self, ticker)-> Stock: 
        return self.stockandtickers.get(ticker)
        
