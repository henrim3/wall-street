from __future__ import annotations
from action import Action
from player import Player
from team import Team
from stock_market.stock import Stock
from stock_market.stock_market import StockMarket
from turn.golden_opportunity_turn import GoldenOpportunityStock


class RealPlayer(Player):
    def __init__(self, name: str, initial_capital: int, percentage_stake: int):
        self.name: str = name
        self.capital: int = initial_capital
        self.percentage_stake: int = percentage_stake
        self.portfolio: dict[str, int] = {}  # {stock: quantity}
        self.team: Team = None
        self.stock_market: StockMarket = None  # Initialize as None
        self.is_active: bool = True  # New attribute to track if the player is active

    def setTeam(self, team: Team) -> None:
        self.team = team

    def setStockMarket(self, stock_market: StockMarket) -> None:
        self.stock_market = stock_market

    def check_portfolio(self, stock_market: StockMarket, indent=2):
        # Ensure that stock_market is not None
        if stock_market is None:
            print("Stock market not set.")
            return

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
            if stockobj.isbluechip and self.portfolio[stock] != 0:
                blue.append(stock)
            elif self.portfolio[stock] != 0:
                pennies.append(stock)

        pennies.sort()
        blue.sort()

        for stock in pennies:
            if not reachedpenny:
                print(f"{indentstr}Owned Penny Stocks:")
                reachedpenny = True
            status = "Owned" if stock_market.get_stock(
                stock).owned > stock_market.get_stock(stock).needed else ""
            print(f"{indentstr}{indentstr}{stock}: "
                  f"{self.portfolio[stock]} shares {status}")

        for stock in blue:
            if not reachedblue:
                print(f"{indentstr}Owned Blue Chip Stocks:")
                reachedblue = True
            status = "Owned" if stock_market.get_stock(
                stock).owned > stock_market.get_stock(stock).needed else ""
            print(f"{indentstr}{indentstr}{stock}: "
                  f"{self.portfolio[stock]} shares {status}")

        print(f"Total portfolio value: ${total:.2f}")

    def check_team_portfolio(self, stock_market: StockMarket, indent=2):
        if not self.team:
            print("No team assigned.")
            return

        if stock_market is None:
            print("Stock market not set.")
            return

        print(f"{self.team.name}'s Portfolio:")
        indentstr = " " * indent
        team_portfolio = self.team.team_portfolio
        if not team_portfolio:
            print(f"{indentstr}No stocks in team portfolio.")
            return

        for stock_name, quantity in team_portfolio.items():
            stock = stock_market.get_stock(stock_name)
            if stock.owned >= stock.needed:
                percentage = (
                    quantity / stock_market.total_shares(stock_name)) * 100
                status = "Owned" if stock.owned >= stock.needed else ""
                print(f"{indentstr}{stock_name}: "
                      f"{quantity} shares ({percentage:.2f}% of market) {status}")
            else:
                print(f"[DEBUG] Stock "
                      f"{stock_name} does not meet the needed threshold for display.")

    def choose_action(self, actions: list[Action], indent: int = 0) -> Action:
        indent_str: str = " " * indent
        prompt: str = indent_str + "Available Actions:"

        for i, action in enumerate(actions):
            prompt += f"\n  {indent_str}{i}: {action.name}"

        num_actions: int = len(actions)
        user_choice: int
        while True:
            print(prompt)
            raw_input: str = input(indent_str + "Choose an action: ")

            try:
                user_choice: int = int(raw_input)
                if 0 <= user_choice <= num_actions:
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
        if stock_market is None:
            print("Stock market not set.")
            return [None, None]

        stock_market.print_market_status(False)

        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to buy (q to quit): ")
            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                if stock_name == "q":
                    return [None, None]
                print("Invalid stock name.")
                continue
            if stock.shares <= 0:
                print(("No shares available."))
                continue
            quantity: int
            stock.printinfo()
            print("")
            while True:
                maxamt = int(self.capital // stock.price)
                if stock.shares < maxamt:
                    maxamt = stock.shares
                tmp: str = input(f"Enter the quantity you want to buy (up to "
                                 f"{maxamt}) (q to quit): ").strip()
                try:
                    quantity = int(tmp)
                except ValueError:
                    if tmp == "q":
                        return [None, None]
                    print("Quantity should be a number.")
                    continue

                if quantity < 1:
                    print("Quantity must be >= 1")
                    continue

                break

            total_price: int = stock.price * quantity

            if total_price > self.capital:
                print("Not enough capital")
                continue

            elif quantity > stock.shares:
                print(f"{stock.ticker} only has "
                      f"{stock.shares} available shares.")
                continue

            return stock_name, quantity

    def choose_sell_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        if stock_market is None:
            print("Stock market not set.")
            return [None, None]

        self.check_portfolio(stock_market)
        empty: bool = True
        for key in self.portfolio.keys():
            if self.portfolio[key] != 0:
                empty = False
        if not self.portfolio or empty:
            print("No shares available to sell")
            return [None, None]
        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to sell (q to quit): ")

            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                if stock_name == "q":
                    return [None, None]
                print("Invalid stock name.")
                continue

            quantity_available = self.portfolio.get(stock_name)

            quantity: int

            if quantity_available is None or quantity_available == 0:
                print(f"No shares of {stock_name} available to sell.")
                continue
            while True:
                tmp: str = input(f"Enter the quantity you want to sell (up to "
                                 f"{quantity_available}) (q to quit): ")
                try:

                    quantity = int(tmp)
                except ValueError:
                    if tmp == "q":
                        return [None, None]
                    continue

                if quantity < 1 or quantity > quantity_available:
                    print(f"Quantity must be 1-{quantity_available}")
                    continue

                break



            return stock_name, quantity

    def choose_get_info(self, stock_market: StockMarket) -> Stock:
        if stock_market is None:
            print("Stock market not set.")
            return None

        stock_market.print_market_status(False)
        while True:
            stock_name: str = input(
                "Enter the name of the stock you want to get information on (q to quit): ")
            stock: Stock = stock_market.get_stock(stock_name)
            if stock is None:
                if stock_name == "q":
                    return None
                print("Invalid stock name.")
                continue
            return stock

    def choose_go_investment_amount(self, go_stock: GoldenOpportunityStock) -> float:
        print("Golden Opportunity:")
        print(go_stock)
        print()
        while True:
            print(f"Your Capital: {self.capital}\n")
            input_str: str = input("How much would you like to invest?: ")
            invest_amt: float

            try:
                invest_amt = float(input_str)
            except ValueError:
                print("Input must be a number")
                continue

            if invest_amt < 0 or invest_amt > self.capital:
                print(f"Input must be in range 0-{self.capital}")
                continue

            return invest_amt


    def choose_investment_amount(self, investment_amount: int) -> float:
        while True:
            raw_input: str = input(
                "Enter the amount you want to invest (q to quit): ")
            try:
                amount: float = float(raw_input)
                if amount > 0 and amount <= investment_amount:
                    return amount
                print(f"Amount must be > 0 and <= {investment_amount}.")
            except ValueError:
                if raw_input == "q":
                    return 0.0
                print("Invalid input. Enter a number.")

        return 0.0
