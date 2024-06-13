from stock_market import StockMarket


class Player:
    def __init__(self, name, initial_capital, percentage_stake):
        self.name = name
        self.capital = initial_capital
        self.percentage_stake = percentage_stake
        self.portfolio = {}  # {stock_name: quantity}

    def buy_stock(self, stock_name, quantity, stock_price):
        total_cost = quantity * stock_price
        if self.capital >= total_cost:
            if stock_name in self.portfolio:
                self.portfolio[stock_name] += quantity
            else:
                self.portfolio[stock_name] = quantity
            self.capital -= total_cost
            print(f"{self.name} bought {quantity} shares of {stock_name} at ${stock_price} each.")
        else:
            print(f"{self.name} does not have enough capital to buy {quantity} shares of {stock_name}.")

    def sell_stock(self, stock_name, quantity, stock_price):
        if stock_name in self.portfolio and self.portfolio[stock_name] >= quantity:
            self.portfolio[stock_name] -= quantity
            self.capital += quantity * stock_price
            print(f"{self.name} sold {quantity} shares of {stock_name} at ${stock_price} each.")
        else:
            print(f"{self.name} does not have {quantity} shares of {stock_name} to sell.")

    def check_portfolio(self):
        print(f"{self.name}'s Portfolio:")
        for stock, quantity in self.portfolio.items():
            print(f"{stock}: {quantity} shares")

    def allocate_to_buyout_fund(self, amount):
        if amount <= self.capital:
            self.capital -= amount
            print(f"{self.name} allocated ${amount} to the Buyout Fund.")
            return amount
        else:
            print(f"{self.name} does not have enough capital to allocate ${amount} to the Buyout Fund.")
            return 0

    def receive_dividend(self, stock_name, dividend_amount):
        if stock_name in self.portfolio:
            self.capital += dividend_amount
            print(f"{self.name} received a dividend of ${dividend_amount} for {stock_name}.")
        else:
            print(f"{self.name} does not own {stock_name} shares to receive dividends.")

    def liquidate_portfolio(self):
        total_value = sum(self.portfolio[stock] * stock_price for stock, stock_price in StockMarket.stocks.items())
        self.capital += total_value
        self.portfolio.clear()
        print(f"{self.name} liquidated their portfolio and received ${total_value}.")

    def __str__(self):
        return f"Player {self.name}: Capital ${self.capital}, Portfolio {self.portfolio}"
