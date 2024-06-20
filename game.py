from player import Player
from stock_market import StockMarket
from user_input import choice_input

TURN_ACTIONS = [
    "Buy Stock",
    "Sell Stock",
    "Check Portfolio",
    "Allocate to Buyout Fund",
    "Skip Turn",
]


class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.stock_market = StockMarket()

    def initialize_game(self):
        self.stock_market.initialize_stocks()
        self.stock_market.print_market_status()
        self.players = [
            Player("Player 1", 1000.0, 33.33),
            Player("Player 2", 1000.0, 33.33),
            Player("Player 3", 1000.0, 33.33),
        ]

    def play_build_phase(self):
        print("Build Phase Begins:")
        for turn in range(3):
            print(f"Turn {turn + 1}:")
            self.stock_market.fluctuate_market()
            self.stock_market.print_market_status()
            for player in self.players:
                self.player_turn(player)

    def player_turn(self, player):
        print(f"-------------{player.name}'s TURN-------------")
        action: str = choice_input(
            TURN_ACTIONS, "Choose an action: ", "Actions")[1]

        if action == "Buy Stock":
            self.buy_stock_action(player)
        elif action == "Sell Stock":
            self.sell_stock_action(player)
        elif action == "Check Portfolio":
            player.check_portfolio()
        elif action == "Allocate to Buyout Fund":
            amount = float(input("Enter amount to allocate to Buyout Fund: "))
            player.allocate_to_buyout_fund(amount)
        elif action == "Skip Turn":
            print(f"{player.name} skipped their turn.")
        print()

    def buy_stock_action(self, player):
        self.stock_market.print_market_status()
        stock_name = input("Enter the name of the stock you want to buy: ")
        quantity = int(input("Enter the quantity you want to buy: "))
        if stock_name in self.stock_market.stocks:
            stock_price = self.stock_market.stocks[stock_name]
            player.buy_stock(stock_name, quantity, stock_price)
        else:
            print("Invalid stock name.")

    def sell_stock_action(self, player):
        player.check_portfolio()
        stock_name = input("Enter the name of the stock you want to sell: ")
        quantity = int(input("Enter the quantity you want to sell: "))
        if stock_name in self.stock_market.stocks:
            stock_price = self.stock_market.stocks[stock_name]
            player.sell_stock(stock_name, quantity, stock_price)
        else:
            print("Invalid stock name.")

    def play_golden_opportunity_phase(self):
        print("Golden Opportunity Phase Begins:")
        # Logic for Golden Opportunity Phase

    def end_game(self):
        print("Game Over. Final Portfolios:")
        for player in self.players:
            player.check_portfolio()
        print("Thank you for playing!")

    def run(self):
        self.initialize_game()
        self.play_build_phase()
        self.play_golden_opportunity_phase()
        self.end_game()


if __name__ == "__main__":
    game = Game(num_players=3)
    game.run()
