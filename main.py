from stock_market.stock_market import StockMarket
from team import Team
from turn import BuildTurn, GoldenOpportunityTurn, run_turns
from player.real_player import RealPlayer
from Datacollector import dataCollector

NUM_BUILD_TURNS = 10
NUM_GO_TURNS = 1

def determine_winner(teams: list[Team], stock_market: StockMarket) -> None:
    team_percentages = {}

    for team in teams:
        # Calculate and print the team's market percentage
        team.check_team_portfolio(stock_market)
        total_percentage = sum(
            stock_market.get_stock(stock_name).stockrep * 100
            for stock_name in team.team_portfolio
        )
        team_percentages[team.name] = total_percentage
        print(f"{team.name} controls {total_percentage:.2f}% of the market.")

    # Determine the winning team
    winning_team = max(team_percentages, key=team_percentages.get)
    print(f"\nThe winning team is {winning_team} with {team_percentages[winning_team]:.2f}% of the market!")

if __name__ == "__main__":
    team1 = Team(
        "Team 1",
        [
            RealPlayer("Bob", 10000, 3),
            RealPlayer("Avery", 10000, 3),
            RealPlayer("Jeff", 10000, 3),
        ]
    )

    team2 = Team(
        "Team 2",
        [
            RealPlayer("Frank", 10000, 3),
            RealPlayer("Croc", 10000, 3),
            RealPlayer("Ghost", 10000, 3),
        ]
    )

    data = dataCollector([team1,team2])

    teams: list[Team] = [team1, team2]

    stock_market = StockMarket()
    stock_market.initialize_stocks()

    # Set the market condition to 'normal' for all stocks
    for stock in stock_market.stocks:
        stock.set_market_condition('normal')

    build_turn: BuildTurn = BuildTurn(teams, stock_market, data)
    go_turn: GoldenOpportunityTurn = GoldenOpportunityTurn(teams, stock_market)

    turns = [
        [build_turn, NUM_BUILD_TURNS],
        [go_turn, NUM_GO_TURNS],
    ]

    run_turns(turns)

    # Determine the winner after all turns are completed
    determine_winner(teams, stock_market)
    data.plotdata()
