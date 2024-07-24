from action import Action
from player import Player
from stock import Stock
from stock_market import StockMarket


class RealPlayer(Player):
    def __init__(self, name: str, initial_capital: int, percentage_stake: int):
        self.name: str = name
        self.capital: int = initial_capital
        self.percentage_stake: int = percentage_stake
        self.portfolio: dict[str, int] = {}  # {stock: quantity}
        self.transactions: list = []

    def check_portfolio(self):
        print(f"{self.name}'s Portfolio:")
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
            raw_input: str = input(indent_str + "Choose an action: ")

            try:
                user_choice: int = int(raw_input)
                if user_choice >= 0 and user_choice <= num_actions:
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

        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to buy: ")
            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                print("Invalid stock name.")
                continue

            quantity: int
            while True:
                try:
                    quantity = int(
                        input("Enter the quantity you want to buy: "))
                except TypeError:
                    continue

                if quantity < 1:
                    print("Quantity must be >= 1")
                    continue

                break

            total_price: int = stock.price * quantity

            if total_price > self.capital:
                print("Not enough capital")
                continue

            return stock_name, quantity

    def choose_sell_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        self.check_portfolio()

        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to sell: ")

            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                print("Invalid stock name.")
                continue

            quantity_available = self.portfolio[stock_name]

            quantity: int
            while True:
                try:
                    quantity = int(
                        input("Enter the quantity you want to sell: "))
                except TypeError:
                    continue

                if quantity < 1 or quantity > quantity_available:
                    print(f"Quantity must be 1-{quantity_available}")
                    continue

                break

            return stock_name, quantity
