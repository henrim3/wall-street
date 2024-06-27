from player import Player
from stock_market import StockMarket

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.stock_market = StockMarket()

    def initialize_game(self):
        self.stock_market.initialize_stocks()
        self.stock_market.print_market_status(True)
        self.players = [
            Player("Player 1", 1000.0, 33.33),
            Player("Player 2", 1000.0, 33.33),
            Player("Player 3", 1000.0, 33.33),
        ]

    def play_build_phase(self):
        print("Build Phase Begins:\n")
        for turn in range(3):
            print(f"Turn {turn + 1}:\n")
            self.stock_market.fluctuate_market()
            self.stock_market.print_market_status(False)
            for player in self.players:
                self.player_turn(player)

    def player_turn(self, player):
        print(f"{player.name}'s turn:")
        print(f"\t Current capital: {player.capital}")
        print(f"\t Current percentage stake: {player.percentage_stake} \n")
        action  = 0
        while action != 6:
            print("Actions: 1) Buy Stock  2) Sell Stock  3) Get Stock Info 4) Check Portfolio  5) Allocate to Buyout Fund  6) Skip Turn")
            action = input("\nChoose an action (1-5): ")
            print("")
            if action == "1":
                self.buy_stock_action(player)
            elif action == "2":
                self.sell_stock_action(player)
            elif action == "3":
                stockname = input("Enter stock tikr:")
                if(stockname in self.stock_market.stockandtikrs):
                    stock = self.stock_market.get_stock(stockname)
                    stock.printinfo()
                else:
                    print(f"Stock tikr {stockname} not found")
            elif action == "4":
                player.check_portfolio()
            elif action == "5":
                amount = float(input("Enter amount to allocate to Buyout Fund: "))
                player.allocate_to_buyout_fund(amount)
            elif action == "6":
                print(f"{player.name} skipped their turn.")
                break
            else:
                print("Invalid command")

    def buy_stock_action(self, player):
        self.stock_market.print_market_status(False)
        tikr = input("Enter the tikr of the stock you want to buy: ")
        quantity = int(input("Enter the quantity you want to buy: "))
        if tikr in self.stock_market.stockandtikrs:
            curstock = self.stock_market.get_stock(tikr)
            player.buy_stock(curstock, quantity)
        else:
            print("Invalid stock name.")

    def sell_stock_action(self, player):
        player.check_portfolio()
        stock_tikr = input("Enter the tikr of the stock you want to sell: ")
        quantity = int(input("Enter the quantity you want to sell: "))
        if stock_tikr in self.stock_market.stockandtikrs:
            curstock = self.stock_market.get_stock(stock_tikr)
            player.sell_stock(curstock, quantity)
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
