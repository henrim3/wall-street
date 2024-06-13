from stock_market import StockMarket
from stock import Stock


class Player:
    def __init__(self, name, initial_capital, percentage_stake):
        self.name = name
        self.capital = initial_capital
        self.percentage_stake = percentage_stake
        self.portfolio = {}  # {stock: quantity}

    def buy_stock(self, stock, quantity):
        total_cost = quantity * stock.price
        if self.capital >= total_cost:
            if stock in self.portfolio:
                self.portfolio[stock] += quantity
            else:
                self.portfolio[stock] = quantity
            self.capital -= total_cost
            print(f"{self.name} bought {quantity} shares of {stock.symbol}: {stock.name} at ${stock.price} each.")
        else:
            print(f"{self.name} does not have enough capital to buy {quantity} shares of {stock.name}.")

    def sell_stock(self, stock, quantity):
        if stock.name in self.portfolio and self.portfolio[stock.name] >= quantity:
            self.portfolio[stock.name] -= quantity
            self.capital += quantity * stock.price
            print(f"{self.name} sold {quantity} shares of {stock.name} at ${stock.price} each.")
        else:
            print(f"{self.name} does not have {quantity} shares of {stock.name} to sell.")

    def check_portfolio(self):
        print(f"{self.name}'s Portfolio:")
        for stock, quantity in self.portfolio.items():
            print(f"{stock.name}: {quantity} shares, worth {quantity * self.price}")

    def allocate_to_buyout_fund(self, amount):
        if amount <= self.capital:
            self.capital -= amount
            print(f"{self.name} allocated ${amount} to the Buyout Fund.")
            return amount
        else:
            print(f"{self.name} does not have enough capital to allocate ${amount} to the Buyout Fund.")
            return 0

    def receive_dividend(self, stock, dividend_amount):
        if stock in self.portfolio:
            self.capital += dividend_amount
            print(f"{self.name} received a dividend of ${dividend_amount} for {stock.name}.")
        else:
            print(f"{self.name} does not own {stock.name} shares to receive dividends.")

    def liquidate_portfolio(self):
        total_value = sum(self.portfolio[stock] * stock.price for stock, stock_price in self.portfolio)
        self.capital += total_value
        self.portfolio.clear()
        print(f"{self.name} liquidated their portfolio and received ${total_value}.")
        
    def __str__(self):
        return f"Player {self.name}: Capital ${self.capital}, Portfolio {self.portfolio}"
