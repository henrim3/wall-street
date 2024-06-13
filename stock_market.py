class StockMarket:
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
        print("Current Stock Prices:")
        for stock, price in self.stocks.items():
            print(f"{stock}: ${price:.2f}")
