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

        print(prompt)
        print("\nchoosing action...")
        time.sleep(2)

        # user_choice: int = 0
        user_choice: int = random.randint(0, num_actions)

        print("the choice was:", user_choice)
        time.sleep(2)

        return actions[user_choice]

    def choose_buy_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        stock_market.print_market_status(False)

        stocks_dict = stock_market.get_stocks()

        print("Choosing which stock to buy")
        time.sleep(2)
        keys = list(stocks_dict.keys())
        stock_tik = random.choice(keys)
        print("stock chosen is(ticker):", stock_tik)
        stock = stocks_dict.get(stock_tik)
        stock_name = stock.name
        print("stock chosen is:", stock_name)
        time.sleep(2)

        while True:

            quantity: int = random.randint(1, 500)
            print("Trying to buy {} stocks".format(quantity))
            time.sleep(2)

            total_price: int = stock.price * quantity

            if total_price > self.capital:
                print("Not enough capital")
                time.sleep(2)
                continue
            break

        return stock_tik, quantity

    def choose_sell_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        self.check_portfolio()

        if (len(self.portfolio) == 0):
            print("Portfolio Empty!")
            time.sleep(2)
            return None

        # choosing a stock to sell
        stocks_owned = list(self.portfolio.keys())
        stock_to_sell = random.choice(stocks_owned)
        amount_to_sell = random.randint(1, self.portfolio[stock_to_sell])
        print("stock that will be sold: {}  amount: {}".format(
            stock_to_sell, amount_to_sell))

        return stock_to_sell, amount_to_sell

    def choose_get_info(self, stock_market: StockMarket) -> str:
        stock_market.print_market_status(False)

        stocks_dict = stock_market.get_stocks()

        keys = list(stocks_dict.keys())
        stock_tik = random.choice(keys)
        time.sleep(2)
        print("stock chosen is(ticker):", stock_tik)

        stock = stocks_dict.get(stock_tik)

        stock_name = stock.name

        stock: Stock = stock_market.get_stock(stock_tik)
        print("stock chosen is:", stock_name)
        time.sleep(2)

        return stock
