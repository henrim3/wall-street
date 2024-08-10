import random
from stock_market import StockMarket
from team import Team
from turn import Turn
from player import Player

# range of percentages for golden opportunity stock price
TEAM_CAP_PERC_RANGE = 0.2, 0.4


class GoldenOpportunityTurn(Turn):
    def __init__(self, teams: list[Team], stock_market: StockMarket) -> None:
        self.name: str = "Golden Opportunity Turn"
        self.teams: list[Team] = teams
        self.stock_market: StockMarket = stock_market

    def run(self, turn_number: int) -> None:
        for team in self.teams:
            # require investment based on percentage of team capital
            percentage: float = random.uniform(
                TEAM_CAP_PERC_RANGE[0], TEAM_CAP_PERC_RANGE[1])
            stock_price: float = team.get_total_capital() * percentage

            go_stock = GoldenOpportunityStock("?", "????", stock_price)
            investment_needed: float = 10000
            team_total_investment: float = 0
            player_investments: dict[Player, float] = {}
            for player in team.players:
                print(player.name)
                self.output(turn_number)
                player_investment: float = player.choose_go_investment_amount(
                    go_stock)
                player_investments[player] = player_investment
                team_total_investment += player_investment

            if team_total_investment < investment_needed:
                print("Investment unsuccessful\n")
            else:
                print("Investment successful\n")
                # take capital from players
                for player, investment_amt in player_investments.items():
                    player.capital -= investment_amt

                # add stock to team portfolio
                team.go_stocks.append(go_stock)


class GoldenOpportunityStock():
    def __init__(self, name: str, ticker: str, price: float):
        self.name: str = name
        self.ticker: str = ticker
        self.price: float = price

    def __str__(self):
        return f"\nName: {self.name}\n" + \
            f"Ticker: {self.ticker}\n"
