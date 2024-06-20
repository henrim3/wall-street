from player import Player
from stock_market import StockMarket

# dfsdf

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
        self.stock_market.print_market_status()
        self.players = [
            Player("Player 1", 1000.0, 33.33),
            Player("Player 2", 1000.0, 33.33),
            Player("Player 3", 1000.0, 33.33),
        ]

    def play_build_phase(self):
        print(f"{self.RETRO_GREEN}Build Phase Begins:{self.END_COLOR}")
        for turn in range(3):
            print(f"\n{self.RETRO_GREEN}=== Turn {turn + 1} ==={self.END_COLOR}")
            self.stock_market.fluctuate_market()
            self.stock_market.print_market_status()
            for player in self.players:
                print(f"\n{self.RETRO_GREEN}--------------------{self.END_COLOR}")
                self.player_turn(player)
                print(f"{self.RETRO_GREEN}--------------------{self.END_COLOR}\n")

    def player_turn(self, player):
        while True:
            print(f"\n{self.RETRO_GREEN}{player.name}'s turn:{self.END_COLOR}")
            print("Actions: 1) Buy Stock  2) Sell Stock  3) Check Portfolio  4) Allocate to Buyout Fund  5) Check Stake  6) Skip Turn")
            action = input("Choose an action (1-6): ")

            if action == "1":
                if self.buy_stock_action(player):
                    break
            elif action == "2":
                if self.sell_stock_action(player):
                    break
            elif action == "3":
                player.check_portfolio()
            elif action == "4":
                amount = float(input("Enter amount to allocate to Buyout Fund: "))
                player.allocate_to_buyout_fund(amount)
            elif action == "5":
                player.check_stake()
            elif action == "6":
                print(f"{self.RETRO_GREEN}{player.name} skipped their turn.{self.END_COLOR}")
                break

    def buy_stock_action(self, player):
        self.stock_market.print_market_status()
        stock_name = input("Enter the name of the stock you want to buy: ")
        if stock_name not in self.stock_market.stocks:
            print(f"{self.RETRO_GREEN}Invalid stock name. Please try again.{self.END_COLOR}")
            return False
        quantity = int(input("Enter the quantity you want to buy: "))
        stock_price = self.stock_market.stocks[stock_name]
        player.buy_stock(stock_name, quantity, stock_price)
        return True

    def sell_stock_action(self, player):
        player.check_portfolio()
        stock_name = input("Enter the name of the stock you want to sell: ")
        if stock_name not in self.stock_market.stocks:
            print(f"{self.RETRO_GREEN}Invalid stock name. Please try again.{self.END_COLOR}")
            return False
        quantity = int(input("Enter the quantity you want to sell: "))
        stock_price = self.stock_market.stocks[stock_name]
        player.sell_stock(stock_name, quantity, stock_price)
        return True

    def play_golden_opportunity_phase(self):
        print(f"{self.RETRO_GREEN}Golden Opportunity Phase Begins:{self.END_COLOR}")
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
