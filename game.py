from player import Player
from stock_market import StockMarket
from user_input import choice_input

TURN_ACTIONS = [
    "Buy Stock",
    "Sell Stock",
    "Get Stock Info",
    "Check Portfolio",
    "Allocate to Buyout Fund",
    "End Turn"
]


class Game:
    RETRO_GREEN = "\033[92m"
    END_COLOR = "\033[0m"
    
    ascii_art_title = """

          _____                    _____                    _____     _____                    _____             _____                    _____                    _____                    _____             _____          
         /\    \                  /\    \                  /\    \   /\    \                  /\    \           /\    \                  /\    \                  /\    \                  /\    \           /\    \         
        /::\____\                /::\    \                /::\____\ /::\____\                /::\    \         /::\    \                /::\    \                /::\    \                /::\    \         /::\    \        
       /:::/    /               /::::\    \              /:::/    //:::/    /               /::::\    \        \:::\    \              /::::\    \              /::::\    \              /::::\    \        \:::\    \       
      /:::/   _/___            /::::::\    \            /:::/    //:::/    /               /::::::\    \        \:::\    \            /::::::\    \            /::::::\    \            /::::::\    \        \:::\    \      
     /:::/   /\    \          /:::/\:::\    \          /:::/    //:::/    /               /:::/\:::\    \        \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \        \:::\    \     
    /:::/   /::\____\        /:::/__\:::\    \        /:::/    //:::/    /               /:::/__\:::\    \        \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        \:::\    \    
   /:::/   /:::/    /       /::::\   \:::\    \      /:::/    //:::/    /                \:::\   \:::\    \       /::::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \       /::::\    \   
  /:::/   /:::/   _/___    /::::::\   \:::\    \    /:::/    //:::/    /               ___\:::\   \:::\    \     /::::::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \     /::::::\    \  
 /:::/___/:::/   /\    \  /:::/\:::\   \:::\    \  /:::/    //:::/    /               /\   \:::\   \:::\    \   /:::/\:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \   /:::/\:::\    \ 
|:::|   /:::/   /::\____\/:::/  \:::\   \:::\____\/:::/____//:::/____/               /::\   \:::\   \:::\____\ /:::/  \:::\____\/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/__\:::\   \:::\____\ /:::/  \:::\____\
|:::|__/:::/   /:::/    /\::/    \:::\  /:::/    /\:::\    \\:::\    \               \:::\   \:::\   \::/    //:::/    \::/    /\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\:::\   \:::\   \::/    //:::/    \::/    /
 \:::\/:::/   /:::/    /  \/____/ \:::\/:::/    /  \:::\    \\:::\    \               \:::\   \:::\   \/____//:::/    / \/____/  \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____//:::/    / \/____/ 
  \::::::/   /:::/    /            \::::::/    /    \:::\    \\:::\    \               \:::\   \:::\    \   /:::/    /                 |:::::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \   /:::/    /          
   \::::/___/:::/    /              \::::/    /      \:::\    \\:::\    \               \:::\   \:::\____\ /:::/    /                  |::|\::::/    /      \:::\   \:::\____\       \:::\   \:::\____\ /:::/    /           
    \:::\__/:::/    /               /:::/    /        \:::\    \\:::\    \               \:::\  /:::/    / \::/    /                   |::| \::/____/        \:::\   \::/    /        \:::\   \::/    / \::/    /            
     \::::::::/    /               /:::/    /          \:::\    \\:::\    \               \:::\/:::/    /   \/____/                    |::|  ~|               \:::\   \/____/          \:::\   \/____/   \/____/             
      \::::::/    /               /:::/    /            \:::\    \\:::\    \               \::::::/    /                               |::|   |                \:::\    \               \:::\    \                           
       \::::/    /               /:::/    /              \:::\____\\:::\____\               \::::/    /                                \::|   |                 \:::\____\               \:::\____\                          
        \::/____/                \::/    /                \::/    / \::/    /                \::/    /                                  \:|   |                  \::/    /                \::/    /                          
         ~~                       \/____/                  \/____/   \/____/                  \/____/                                    \|___|                   \/____/                  \/____/                           
                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                            


"""
    
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.stock_market = StockMarket()

    def print_title(self):
        print(f"{self.RETRO_GREEN}{self.ascii_art_title}{self.END_COLOR}")

    def initialize_game(self):
        self.print_title()
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
                print(f"\n{self.RETRO_GREEN}--------------------{self.END_COLOR}")
                self.player_turn(player)
                print(f"{self.RETRO_GREEN}--------------------{self.END_COLOR}\n")

    def player_turn(self, player):
        print(f"-------------{player.name}'s TURN-------------")
        print(f"\nCaptial: ${player.capital}")
        while(True):
            action: str = choice_input(
                TURN_ACTIONS, "Choose an action: ", "Actions")[1]
            if action == "Buy Stock":
                self.buy_stock_action(player)
            elif action == "Sell Stock":
                self.sell_stock_action(player)
            elif action == "Check Portfolio":
                player.check_portfolio()
            elif action == "Allocate to Buyout Fund":
                inp = input(f"Enter amount to allocate to Buyout Fund (up to ${player.capital:.2f}): ")
                try:
                    amount = float(inp)
                    player.allocate_to_buyout_fund(amount)
                except ValueError:
                    print("Error: Invalid amount.")
            elif action == "End Turn":
                print(f"{player.name} completed their turn.")
                break
            elif action == "Get Stock Info":
                stockname = input("Enter stock ticker:")
                if(stockname in self.stock_market.stockandtickers):
                    stock = self.stock_market.get_stock(stockname)
                    stock.printinfo()
                else:
                    print(f"Error: Stock ticker {stockname} not found")
        print()

    def buy_stock_action(self, player):
        self.stock_market.print_market_status(False)
        ticker = input("Enter the ticker of the stock you want to buy: ")
        if ticker in self.stock_market.stockandtickers:
            curstock = self.stock_market.get_stock(ticker)
            maxamt = int(player.capital // curstock.price)
            inp = input(f"Enter the quantity you want to buy (up to {maxamt}): ")
            if inp.isdigit():
                quantity = int(inp)
                player.buy_stock(curstock, quantity)
            else:
                print("Error: Invalid input.")
        else:
            print("Error: Invalid input.")

    def sell_stock_action(self, player):
        player.check_portfolio()
        stock_ticker = input("\nEnter the ticker of the stock you want to sell: ")
        if stock_ticker in self.stock_market.stockandtickers:
            curstock = self.stock_market.get_stock(stock_ticker)
            if curstock in player.portfolio:
                inp = input(f"Enter the quantity you want to sell (up to {player.portfolio[curstock]}): ")
                if inp.isdigit():
                    quantity = int(inp)
                    player.sell_stock(curstock, quantity)
                else:
                    print("Error: Invalid input.")
            else:
                print(f"No shares of {stock_ticker} owned.")
        else:
            print("Error: Invalid input.")
            

    def play_golden_opportunity_phase(self):
        print("Golden Opportunity Phase Begins:")
        # Logic for Golden Opportunity Phase

    def end_game(self):
        print(f"{self.RETRO_GREEN}Game Over. Final Portfolios:{self.END_COLOR}")
        for player in self.players:
            player.check_portfolio()
        print(f"{self.RETRO_GREEN}Thank you for playing!{self.END_COLOR}")

    def run(self):
        self.initialize_game()
        self.play_build_phase()
        self.play_golden_opportunity_phase()
        self.end_game()


if __name__ == "__main__":
    game = Game(num_players=3)
    game.run()
