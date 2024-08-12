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
        return total_capital

    def update_team_portfolio(self, stock_market: StockMarket, stock_name: str, quantity: int) -> None:
        stock = stock_market.get_stock(stock_name)
        if stock.owned >= stock.needed:
            if stock_name in self.team_portfolio:
                self.team_portfolio[stock_name] += quantity
            else:
                self.team_portfolio[stock_name] = quantity

    def check_team_portfolio(self, stock_market: StockMarket, indent=2) -> None:
        print(f"{self.name} Team Portfolio:")
        indentstr = " " * indent
        total_percentage = 0.0  # Initialize total percentage

        for stock_name, quantity in self.team_portfolio.items():
            stock = stock_market.get_stock(stock_name)
            if stock.owned >= stock.needed:
                percentage = stock.stockrep * 100
                total_percentage += percentage  # Add to total percentage
                status = "Owned" if stock.owned >= stock.needed else ""
                print(f"{indentstr}{stock_name}: {quantity} shares ({percentage:.2f}% of market) {status}")
            else:
                pass

        if not self.team_portfolio:
            print(f"{indentstr}No stocks in team portfolio.")
        else:
            # Print the total percentage
            print(f"\n{indentstr}Total market percentage owned by {self.name} Team: {total_percentage:.2f}%")
