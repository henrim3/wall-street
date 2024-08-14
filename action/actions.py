from action import Action
from player import Player
from stock_market.stock import Stock
from stock_market.stock_market import StockMarket
from stock_market.transaction import Transaction
from player import Player
from team import Team

# Set CompleteTransactions = True to see other teams transactions as well
CompleteTransactions = False
# Set AnonymousTransactions = False to see player name in transaction
AnonymousTransactions = True


class AllocateToBuyoutFund(Action):
    def __init__(self, player: Player, team_players: list[Player]) -> None:
        self.name: str = "Buyout Player"
        self.player: Player = player
        self.team_players: list[Player] = [p for p in team_players if p != player]

    def run(self) -> None:
        # Check if the player's capital is sufficient for a buyout
        if self.player.capital < 70000:
            print(f"{self.player.name} does not have enough capital to buy out another player.")
            return

        # List potential targets for buyout
        target = self.select_target()

        if not target:
            print("No valid target selected.")
            return

        # Perform the buyout
        self.perform_buyout(target)

    def select_target(self) -> Player:
        print("Select a player to buy out:")
        for i, teammate in enumerate(self.team_players, 1):
            print(f"{i}. {teammate.name}")

        # Input to select the target
        choice = int(input("Enter the number of the player you want to buy out: ")) - 1

        if 0 <= choice < len(self.team_players):
            return self.team_players[choice]
        else:
            print("Invalid selection.")
            return None

    def perform_buyout(self, target: Player) -> None:
        buyout_price = self.calculate_buyout_price()

        # Deduct the buyout price from the player's capital
        self.player.capital -= buyout_price

        # Transfer assets from the target to the buyer
        self.transfer_assets(target)

        # Remove all players on the target's team
        self.remove_team_players(target)

        print(f"{self.player.name} has successfully bought out {target.name} and their team for ${buyout_price:.2f}!")

    def calculate_buyout_price(self) -> int:
        # Basic buyout price threshold
        return 70000

    def transfer_assets(self, target: Player) -> None:
        # Transfer portfolio stocks to the buyer's portfolio
        for stock_ticker, quantity in target.portfolio.items():
            if stock_ticker not in self.player.portfolio:
                self.player.portfolio[stock_ticker] = 0
            self.player.portfolio[stock_ticker] += quantity

        # Transfer any remaining capital to the buyer
        self.player.capital += target.capital

        # Clear the target player's assets
        target.portfolio.clear()
        target.capital = 0

    def remove_team_players(self, target: Player) -> None:
        # Logic to remove all players on the target's team
        pass



class BuyStock(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Buy Stock"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        stock_ticker, quantity = self.player.choose_buy_stock(
            self.stock_market)
        
        if stock_ticker is None:
            return

        # decrease player capital
        stock: Stock = self.stock_market.get_stock(stock_ticker)
        total_price: int = stock.price * quantity
        assert self.player.capital >= total_price
        assert stock.shares >= quantity
        self.player.capital -= total_price
        stock.owned += quantity
        stock.shares -= quantity
        self.stock_market.availableshares -= quantity

        print(f"After buying: {stock_ticker} owned = {stock.owned}, shares left = {int(stock.shares)}")

        portfolio: dict = self.player.portfolio

        # add stock to portfolio if doesn't already exist
        if stock_ticker not in portfolio.keys():
            portfolio[stock_ticker] = 0

        # add stock to portfolio
        portfolio[stock_ticker] += quantity

        # Debugging: Print to verify portfolio update
        # print(f"{self.player.name}'s portfolio after buying: {portfolio}")

        # Update team portfolio
        self.player.team.update_team_portfolio(self.stock_market, stock_ticker, quantity)


        #add transaction to market
        transaction: Transaction = Transaction(self.player, stock, quantity, total_price, True)
        self.stock_market.transactions.append(transaction)

        if stock.owned > stock.needed:
            print(f"{self.player.name} now owns {stock_ticker} stock!")

        print(f"Bought {quantity} shares of {stock_ticker}")


class CheckPortfolio(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Check Portfolio"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        self.player.check_portfolio(self.stock_market)


class CheckTeamPortfolio(Action):
    def __init__(self, team: Team, stock_market: StockMarket) -> None:
        self.name: str = "Check Team Portfolio"
        self.team: Team = team
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        self.team.check_team_portfolio(self.stock_market)


class CheckBalance(Action):
    def __init__(self, player: Player) -> None:
        self.name: str = "Check Balance"
        self.player: Player = player

    def run(self) -> None:
        print(f"{self.player.name}'s Current Balance: ${self.player.capital:.2f}")


class GetStockInfo(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Get Stock Information"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        stock: Stock = self.player.choose_get_info(self.stock_market)
        if stock is None:
            return
        stock.printinfo()

class GetTransactionHistory(Action):

    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Get Transaction History"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        print("Transactions:")
        indentstr: str = " " * 2
        for transaction in self.stock_market.transactions:
            player: str = "Player"
            share: str = "shares"
            action: str = "bought"
            if not AnonymousTransactions:
                player = transaction.player.name
            if transaction.quantity == 1:
                share = "share"
            if not transaction.buying:
                action = "sold"
            if (transaction.player.team == self.player.team) or CompleteTransactions:
                print(f"{indentstr}{player} {action} {transaction.quantity} {share} of {transaction.stock.name} for ${transaction.price:.2f}")



class SellStock(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Sell Stock"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        stock_name, quantity = self.player.choose_sell_stock(self.stock_market)

        if stock_name is None or quantity is None:
            return

        # Increase player capital
        stock: Stock = self.stock_market.get_stock(stock_name)
        assert stock is not None
        market_value: int = stock.price
        total_sale: int = market_value * quantity
        self.player.capital += total_sale

        # Increase stock shares available and market shares
        stock.shares += quantity
        stock.owned -= quantity
        self.stock_market.availableshares += quantity

        # Remove from portfolio
        portfolio: dict = self.player.portfolio
        assert stock_name in portfolio.keys()
        assert portfolio[stock_name] >= quantity
        portfolio[stock_name] -= quantity

        # Remove stock from portfolio if no shares left
        if portfolio[stock_name] == 0:
            del portfolio[stock_name]

        # Update team portfolio
        self.player.team.update_team_portfolio(self.stock_market, stock_name, -quantity)

        # Add transaction to market
        transaction: Transaction = Transaction(
            self.player, stock, quantity, total_sale, False
        )
        self.stock_market.transactions.append(transaction)

        print(f"Sold {quantity} shares of {stock_name}")


class TeamPortfolio(Action):
    def __init__(self, stock_market: StockMarket) -> None:
        self.name: str = "Team Portfolio"
        self.stock_market: StockMarket = stock_market

    def calculate_percentage(self, stock_name: str, quantity: int) -> float:
        stock: Stock = self.stock_market.get_stock(stock_name)
        if stock is None or stock.market_cap == 0:
            return 0
        return (stock.stockrep) * 100

    def run(self) -> None:
        print("Team Portfolio:")
        team_portfolio: dict[str, int] = {}

        # Collect stock data
        for stock_name in self.stock_market.get_all_stocks():
            stock: Stock = self.stock_market.get_stock(stock_name)
            if stock.owned > stock.needed:
                percentage = self.calculate_percentage(stock_name, stock.owned)
                team_portfolio[stock_name] = percentage
        print(f"Team portfolio aggregated: {team_portfolio}")
        # Print portfolio
        for stock_name, percentage in team_portfolio.items():
            print(f"{stock_name}: {percentage:.2f}% of the market")


class EndTurn(Action):
    def __init__(self) -> None:
        self.name: str = "End Turn"
        self.end_turn = True

    def run(self) -> None:
        pass

class CheckLeaderboard(Action):
    def __init__(self, teamlist: list[Team], stockmarket: StockMarket ) -> None:
        self.name: str = "Check Leaderboard"
        self.teams: list[Team] = teamlist
        self.market = stockmarket
    def run(self) -> None:
        print("Current market statistics:")
        indentstr: str = " " * 2
        print(f"{indentstr}Volume of the market: {(self.market.availableshares):,} totals shares")
        totalval = 0
        marketval = 0
        for stock in self.market.stocks:
            totalval += stock.price * (stock.shares + stock.owned)
            marketval += stock.price * (stock.shares)
        print(f"{indentstr}Total market value: ${marketval:,.2f}\n")
        team_percentages = {}
        for team in self.teams:
            # Calculate and print the team's market percentage
            team.check_team_portfolio(self.market)
            total_percentage = sum(
                self.market.get_stock(stock_name).stockrep * 100
                for stock_name in team.team_portfolio
            )
            team_percentages[team.name] = total_percentage
            print()

        # Determine the winning team
        winning_team = max(team_percentages, key=team_percentages.get)
        print(f"\n{winning_team} is in the lead with {team_percentages[winning_team]:.2f}% of the market!")