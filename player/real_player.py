from action import Action
from player import Player
from stock_market.stock import Stock
from stock_market.stock_market import StockMarket


class RealPlayer(Player):
    def __init__(self, name: str, initial_capital: int, percentage_stake: int):
        self.name: str = name
        self.capital: int = initial_capital
        self.percentage_stake: int = percentage_stake
        self.portfolio: dict[str, int] = {}  # {stock: quantity}

    def check_portfolio(self, stock_market: StockMarket, indent = 2):
        print(f"{self.name}'s Portfolio:")
        indentstr = " " * indent
        total = 0
        reachedblue = False
        reachedpenny = False
        pennies = []
        blue = []
        for stock in self.portfolio.keys():
            stockobj = stock_market.get_stock(stock)
            total += stockobj.price * self.portfolio[stock]
            if stockobj.isbluechip:
                blue.append(stock)
            else:
                pennies.append(stock)
        pennies.sort()
        blue.sort()
        for stock in pennies:
            if not reachedpenny:
                print(f"{indentstr}Owned Penny Stocks:")
                reachedpenny = True
            print(f"{indentstr}{indentstr}{stock}: {self.portfolio[stock]} shares")
        for stock in blue:
            if not reachedblue:
                print(f"{indentstr}Owned Blue Chip Stocks:")
                reachedblue = True
            print(f"{indentstr}{indentstr}{stock}: {self.portfolio[stock]} shares")
        print(f"Total portfolio value: ${total:.2f}")

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
                print(f"\n{indent_str}Error: Input must be a number\n")
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
                maxamt = int(self.capital // stock.price)
                try:
                    quantity = int(
                        input(f"Enter the quantity you want to buy (up to {maxamt}): "))
                except ValueError:
                    print("Quantity shoud be a number.")
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
        self.check_portfolio(stock_market)
        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to sell: ")

            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                print("Invalid stock name.")
                continue

            quantity_available = self.portfolio.get(stock_name)

            quantity: int
            
            if quantity_available is None:
                print(f"No shares of {stock_name} available to sell.")
                continue
            while True:
                try:
                    quantity = int(
                        input(f"Enter the quantity you want to sell (up to {quantity_available}): "))
                except TypeError:
                    continue

                if quantity < 1 or quantity > quantity_available:
                    print(f"Quantity must be 1-{quantity_available}")
                    continue

                break

            return stock_name, quantity

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
