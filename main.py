from stock_market import StockMarket
from player.real_player import RealPlayer
from player.ai_player import AiPlayer
from team import Team
from turn.build_turn import BuildTurn

if __name__ == "__main__":
    team1 = Team(
        "Team 1",
        [
            AiPlayer("Bob", 10000, 3),
            AiPlayer("Avery", 10000, 3),
            AiPlayer("Jeff", 10000, 3),
        ])

    team2 = Team(
        "Team 2",
        [
            AiPlayer("Frank", 10000, 3),
            AiPlayer("Croc", 10000, 3),
            AiPlayer("Ghost", 10000, 3),
        ])

    stock_market = StockMarket()
    stock_market.initialize_stocks()

    # Set the market condition to 'recession' for all stocks
    for stock in stock_market.stocks:
        stock.set_market_condition('Normal')

    build_turn = BuildTurn([team1, team2], stock_market)

    while True:
        build_turn.run()
