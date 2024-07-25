from stock_market import StockMarket
from stock import Stock


class Player:
    def __init__(self, name, initial_capital, percentage_stake):
        self.name = name
        self.capital = initial_capital
        self.percentage_stake = percentage_stake
        self.portfolio = {}  # {stock: quantity}
        self.transactions = []

    def buy_stock(self, stock, quantity):
        total_cost = quantity * stock.price
        if self.capital >= total_cost:
            if stock in self.portfolio:
                self.portfolio[stock] += quantity
            else:
                self.portfolio[stock] = quantity
            self.capital -= total_cost
            stock.owned += quantity
            self.transactions.append((stock, quantity, total_cost))
            self.capital = round(float(self.capital), 2)
            print(f"\n{self.name} bought {quantity} shares of {stock.ticker}: {stock.name} at ${stock.price:.2f} each. \n")
        else:
            print(f"\n{self.name} does not have enough capital to buy {quantity} shares of {stock.name}. \n")

    def sell_stock(self, stock: Stock, quantity):
        if stock in self.portfolio and self.portfolio[stock] >= quantity:
            total_cost = quantity * stock.price
            self.portfolio[stock] -= quantity
            self.transactions.append((stock, quantity, total_cost))
            self.capital = round(float(self.capital), 2)
            print(f"\n{self.name} sold {quantity} shares of {stock.name} at ${stock.price:.2f} each.\n")
        else:
            print(f"\n{self.name} does not have {quantity} shares of {stock.name} to sell.\n")
            
    def check_balance(self):
        print(f"{self.name}'s current balance is: ${self.capital:.2f}")

    def check_portfolio(self):
        print(f"{self.name}'s Portfolio:")
        print(f"${self.capital}, {self.percentage_stake}% percentage stake")
        for stock, quantity in self.portfolio.items():
            print(f"{stock.ticker}: {stock.name}: {quantity} shares, worth {(quantity * stock.price):.2f}")

    def check_transactions(self):
        print(f"{self.name}'s Transactions:")
        for transaction in self.transactions:
            asset, quantity, price = transaction
            if (isinstance(asset, str)):
                print(f"{asset}: ${price}")
            else:
                print(f"{asset.ticker}: {quantity}, ${price}")

    def allocate_to_buyout_fund(self, amount):
        if amount <= self.capital:
            self.capital -= amount
            print(f"{self.name} allocated ${amount} to the Buyout Fund. \n")
            self.transactions.append(("Buyout Fund", 1, amount))
            return amount
        else:
            print(f"{self.name} does not have enough capital to allocate ${amount} to the Buyout Fund. \n")
            return 0

    def receive_dividend(self, stock, dividend_amount)-> None:
        if stock in self.portfolio:
            self.capital += dividend_amount
            print(f"{self.name} received a dividend of ${dividend_amount} for {stock.name}. \n")
            self.transactions.append(("Dividend", 1, dividend_amount))
        else:
            print(f"{self.name} does not own {stock.name} shares to receive dividends. \n")

    def liquidate_portfolio(self):
        stockcount = len(self.portfolio)
        total_value = sum(self.portfolio[stock] * stock.price for stock, stock_price in self.portfolio)
        self.capital += total_value
        self.portfolio.clear()
        self.transactions.append(("Liquidated", stockcount, total_value))
        print(f"{self.name} liquidated their portfolio and received ${total_value:.2f}. \n")

    def __str__(self):
        return f"Player {self.name}: Capital ${self.capital}, Portfolio {self.portfolio}"
