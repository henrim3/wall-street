from stock_market.stock_market import StockMarket
from player.real_player import RealPlayer
# from player.ai_player import AiPlayer
from player.cheap_player import CheapPlayer
from team import Team
from turn.build_turn import BuildTurn

if __name__ == "__main__":
    team1 = Team(
        "Team 1",
        [
            CheapPlayer("Bob", 10000, 3),
            CheapPlayer("Avery", 10000, 3),
            CheapPlayer("Jeff", 10000, 3),
        ])

    team2 = Team(
        "Team 2",
        [
            RealPlayer("Frank", 10000, 3),
            RealPlayer("Croc", 10000, 3),
            RealPlayer("Ghost", 10000, 3),
        ])

    stock_market = StockMarket()
    stock_market.initialize_stocks()

    # Set the market condition to 'recession' for all stocks
    for stock in stock_market.stocks:
        stock.set_market_condition('Normal')

    build_turn = BuildTurn([team1, team2], stock_market)

    while True:
        build_turn.run()
