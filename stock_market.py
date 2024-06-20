class StockMarket:
    BLUE = "\033[94m"
    END_COLOR = "\033[0m"

    def __init__(self):
        self.stocks = {}  # {stock_name: price}

    def initialize_stocks(self):
        self.stocks = {
            "TechCorp": 100.0,
            "HealthInc": 150.0,
            "FinServ": 200.0,
            "EduTech": 80.0,
            "RetailCo": 120.0,
        }

    def fluctuate_market(self):
        import random

        for stock in self.stocks:
            change = random.uniform(-10.0, 10.0)
            self.stocks[stock] += change

    def print_market_status(self):
        print(f"{self.BLUE}Current Stock Prices:{self.END_COLOR}")
        for stock, price in self.stocks.items():
            print(f"{self.BLUE}{stock}: ${price:.2f}{self.END_COLOR}")
