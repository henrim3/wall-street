from __future__ import annotations
from player import Player


class Team:
    def __init__(self, name: str, players: list[Player] = []) -> None:
        self.name: str = name
        self.players: list[Player] = players
        for player in self.players:
            player.setTeam(self)
        self.go_stocks: list = []

    def get_total_capital(self):
        total_capital: float = 0
        for player in self.players:
            total_capital += player.capital
        return total_capital
