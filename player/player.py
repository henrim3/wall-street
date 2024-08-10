from action import Action
from stock_market.stock_market import StockMarket


class Player:
    def __init__(self, name: str, initial_capital: int, percentage_stake: int):
        self.name: str = name
        self.capital: int = initial_capital
        self.percentage_stake: int = percentage_stake
        self.portfolio: dict = {}  # {stock_name: quantity}
        self.team = None

    def setTeam(self, team):
        self.team = team

    def check_portfolio(self, stock_market):
        raise NotImplementedError()

    def choose_action(self, actions: list[Action], indent: int = 0) -> Action:
        raise NotImplementedError()

    def choose_buy_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        raise NotImplementedError()

    def choose_sell_stock(self, stock_market: StockMarket) -> tuple[str, int]:
        raise NotImplementedError()


def choose_go_investment_amount(self, go_stock) -> float:
    raise NotImplementedError()
