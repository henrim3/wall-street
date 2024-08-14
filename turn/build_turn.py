from turn.turn import Turn
from action import Action
from action.actions import AllocateToBuyoutFund, BuyStock, CheckPortfolio, \
    SellStock, EndTurn, CheckBalance, GetStockInfo, GetTransactionHistory, CheckLeaderboard, \
    CheckTeamPortfolio
from team import Team
from stock_market.stock_market import StockMarket
from player import Player  # Make sure you have the Player class imported

class BuildTurn(Turn):
    def __init__(self, teams: list[Team], stock_market: StockMarket) -> None:
        self.name: str = "Build Turn"
        self.teams: list[Team] = teams
        self.stock_market: StockMarket = stock_market

    def run(self, turn_number: int) -> None:
        self.stock_market.fluctuate_market()
        for team in self.teams:
            for player in team.players:
                actions: list[Action] = [
                    BuyStock(player, self.stock_market),
                    SellStock(player, self.stock_market),
                    CheckPortfolio(player, self.stock_market),
                    CheckBalance(player),
                    GetStockInfo(player, self.stock_market),
                    GetTransactionHistory(player, self.stock_market),
                    CheckTeamPortfolio(team, self.stock_market),
                    AllocateToBuyoutFund(player, team.players),
                    CheckLeaderboard(self.teams, self.stock_market),
                    EndTurn(),
                ]


                while True:
                    self.output(turn_number)
                    print(f"[{team.name}] {player.name}'s Turn")

                    action: Action = player.choose_action(actions, 2)
                    action.run()

                    print("\n")

                    if action.end_turn is True:
                        break

                    if action.one_time is True:
                        actions.remove(action)
