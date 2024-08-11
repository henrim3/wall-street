from __future__ import annotations
from player import Player
from stock_market.stock_market import StockMarket
from stock_market import stock

class Team:
    def __init__(self, name: str, players: list[Player] = None) -> None:
        self.name: str = name
        self.players: list[Player] = players if players is not None else []
        for player in self.players:
            player.setTeam(self)
        self.go_stocks: list = []
        self.team_portfolio: dict[str, int] = {}

    def get_total_capital(self) -> float:
        total_capital = sum(player.capital for player in self.players)
        print(f"Total capital for team {self.name}: {total_capital}")
        return total_capital

    def update_team_portfolio(self, stock_market: StockMarket, stock_name: str, quantity: int) -> None:
        stock = stock_market.get_stock(stock_name)
        if stock.owned >= stock.needed:
            if stock_name in self.team_portfolio:
                self.team_portfolio[stock_name] += quantity
            else:
                self.team_portfolio[stock_name] = quantity

            print(f"[DEBUG] Updated Team Portfolio: {self.team_portfolio}")
        else:
            print(f"[DEBUG] Stock {stock_name} does not meet the required owned shares to be added.")

        print(f"[DEBUG] Updated Team Portfolio: {self.team_portfolio}")

        print(f"[DEBUG] Updated Team Portfolio: {self.team_portfolio}")

    def check_team_portfolio(self, stock_market: StockMarket, indent=2) -> None:
        print(f"{self.name} Team Portfolio:")
        indentstr = " " * indent
        for stock_name, quantity in self.team_portfolio.items():
            stock = stock_market.get_stock(stock_name)
            if stock.owned >= stock.needed:
                percentage = (quantity / stock_market.total_shares(stock_name)) * 100
                status = "Owned" if stock.owned >= stock.needed else ""
                print(f"{indentstr}{stock_name}: {quantity} shares ({percentage:.2f}% of market) {status}")
            else:
                print(f"[DEBUG] Stock {stock_name} does not meet the needed threshold for display.")

        if not self.team_portfolio:
            print(f"{indentstr}No stocks in team portfolio.")
