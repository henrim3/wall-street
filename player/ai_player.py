from action import Action
from player import Player
from stock_market.stock import Stock
from stock_market.stock_market import StockMarket
import random
import time


class AiPlayer(Player):
    def __init__(self, name: str, initial_capital: int, percentage_stake: int):
        self.name: str = name
        self.capital: int = initial_capital
        self.percentage_stake: int = percentage_stake
        self.portfolio: dict[str, int] = {}  # {stock: quantity}

    def check_portfolio(self):
        print(f"{self.name}'s Portfolio:")

        if len(self.portfolio.items()) == 0:
            print("empty portfolio!")
            return

        for stock, quantity in self.portfolio.items():
            print(f"{stock}: {quantity} shares")
        print()

    def choose_action(self, actions: list[Action], indent: int = 0) -> Action:
        indent_str: str = " " * indent

        prompt: str = indent_str + "Available Actions:"

        for i, action in enumerate(actions):
            prompt += f"\n  {indent_str}{i}: {action.name}"

        num_actions: int = len(actions) - 1
        user_choice: int
        while True:
            print(prompt)
            # raw_input: str = input(indent_str + "Choose an action: ")
            print("choosing action...")
            time.sleep(3)

            try:
                # user_choice: int = 1
                user_choice: int = random.randint(0, num_actions)
                # user_choice: int = random.randint(0, 1)

                if user_choice >= 0 and user_choice <= num_actions:
                    print("the choice was:", user_choice)
                    print()
                    break
                else:
                    print(
                        f"\n{indent_str}Error: Input must be in range 0-{num_actions}\n")
            except ValueError:
                print("\n{indent_str}Error: Input must be a number\n")
                continue

        return actions[user_choice]

    def choose_buy_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        stock_market.print_market_status(False)

        stocks_dict = stock_market.get_stocks()

        keys = list(stocks_dict.keys())
        stock_tik = random.choice(keys)
        print("stock chosen is(ticker):", stock_tik)
        stock = stocks_dict.get(stock_tik)
        stock_name = stock.name
        print("stock chosen is:", stock_name)

        while True:
            # if stock is None:
            #     print("Invalid stock name.")
            #     continue

            quantity: int

            quantity = random.randint(1, 500)
            if quantity < 1:
                print("Quantity must be >= 1")
                continue

            total_price: int = stock.price * quantity

            if total_price > self.capital:
                print("Not enough capital")
                continue

            break

        return stock_tik, quantity

    def choose_sell_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        self.check_portfolio()

        if (len(self.portfolio) == 0):
            print("Portfolio Empty!")
            return None

        # choosing a stock to sell
        stocks_owned = list(self.portfolio.keys())
        stock_to_sell = random.choice(stocks_owned)
        amount_to_sell = random.randint(1, self.portfolio[stock_to_sell])
        print("stock that will be sold:  amount: {}".format(
            stock_to_sell, amount_to_sell))

        while True:

            stock: Stock = stock_market.get_stock(stock_to_sell)
            if stock is None:
                print("Invalid stock name.")
                continue

            quantity_available = self.portfolio[stock_to_sell]

            while True:

                if amount_to_sell < 1 or amount_to_sell > quantity_available:
                    print(f"Quantity must be 1-{quantity_available}")
                    continue

                break

            return stock_to_sell, amount_to_sell

        def choose_get_info(self, stock_market: StockMarket) -> str:
            stock_market.print_market_status(False)
            while True:
                stock_name: str = input(
                    "Enter the name of the stock you want to get information on: ")
                stock: Stock = stock_market.get_stock(stock_name)
                if stock is None:
                    print("Invalid stock name.")
                    continue
                return stock
