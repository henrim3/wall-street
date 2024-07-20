from turn.turn import Turn
from action import Action
from action.actions import AllocateToBuyoutFund, BuyStock, CheckPortfolio, \
    SellStock, EndTurn
from team import Team
from stock_market import StockMarket


class BuildTurn(Turn):
    def __init__(self, teams: list[Team], stock_market: StockMarket) -> None:
        self.name: str = "Build Turn"
        self.turn_number: int = 1
        self.teams: list[Team] = teams
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        for team in self.teams:
            for player in team.players:
                actions: list[Action] = [
                    BuyStock(player, self.stock_market),
                    SellStock(player, self.stock_market),
                    CheckPortfolio(player),
                    AllocateToBuyoutFund(),
                    EndTurn(),
                ]

                while True:
                    self.output()
                    print(f"[{team.name}] {player.name}'s Turn")

                    action: Action = player.choose_action(actions, 2)
                    action.run()

                    print("\n")

                    if action.end_turn is True:
                        break

                    if action.one_time is True:
                        actions.remove(action)

        self.turn_number += 1