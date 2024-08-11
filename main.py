from stock_market.stock_market import StockMarket
from team import Team
from turn import BuildTurn, GoldenOpportunityTurn, run_turns
from player.real_player import RealPlayer

NUM_BUILD_TURNS = 5
NUM_GO_TURNS = 1

if __name__ == "__main__":
    team1 = Team(
        "Team 1",
        [
            RealPlayer("Bob", 10000, 3),
            RealPlayer("Avery", 10000, 3),
            RealPlayer("Jeff", 10000, 3),
        ])

    team2 = Team(
        "Team 2",
        [
            RealPlayer("Frank", 10000, 3),
            RealPlayer("Croc", 10000, 3),
            RealPlayer("Ghost", 10000, 3),
        ])

    teams: list[Team] = [team1, team2]

    stock_market = StockMarket()
    stock_market.initialize_stocks()

    # Set the market condition to 'recession' for all stocks
    for stock in stock_market.stocks:
        stock.set_market_condition('normal')

    build_turn: BuildTurn = BuildTurn(teams, stock_market)
    go_turn: GoldenOpportunityTurn = GoldenOpportunityTurn(
        teams, stock_market)

    turns = [
        [build_turn, NUM_BUILD_TURNS],
        [go_turn, NUM_GO_TURNS],
    ]

    run_turns(turns)
