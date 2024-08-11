from action import Action
from stock_market.stock import Stock
from stock_market.stock_market import StockMarket
from stock_market.transaction import Transaction
from player import Player

# Set CompleteTransactions = True to see other teams transactions as well
CompleteTransactions = False
# Set AnonymousTransactions = False to see player name in transaction
AnonymousTransactions = True


class AllocateToBuyoutFund(Action):
    def __init__(self) -> None:
        self.name: str = "Allocate to Buyout Fund"

    def run(self) -> None:
        print("running allocate to buyout")


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
        portfolio: dict = self.player.portfolio

        # add stock to portfolio if doesn't already exist
        if stock_ticker not in portfolio.keys():
            portfolio[stock_ticker] = 0

        # add stock to portfolio
        portfolio[stock_ticker] += quantity

        # add transaction to market
        transaction: Transaction = Transaction(
            self.player, stock, quantity, total_price, True)
        self.stock_market.transactions.append(transaction)

        print(f"Bought {quantity} shares of {stock_ticker}")


class CheckPortfolio(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Check Portfolio"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        self.player.check_portfolio(self.stock_market)


class CheckBalance(Action):
    def __init__(self, player: Player) -> None:
        self.name: str = "Check Balance"
        self.player: Player = player

    def run(self) -> None:
        print(
            f"{self.player.name}'s Current Balance: "
            f"${self.player.capital:.2f}"
        )


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
                print(f"{indentstr}{player} {action} {transaction.quantity} "
                      f"{share} of {transaction.stock.name} for ${transaction.price:.2f}")


class SellStock(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Sell Stock"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:

        stock_name, quantity = self.player.choose_sell_stock(self.stock_market)

        if (stock_name is None or quantity is None):
            return

        # increase player capital
        stock: Stock = self.stock_market.get_stock(stock_name)
        assert stock is not None
        market_value: int = stock.price
        total_sale: int = market_value * quantity
        self.player.capital += total_sale

        # Increase stock shares available and marketshares

        stock.shares += quantity
        stock.owned -= quantity
        self.stock_market.availableshares += quantity

        # remove from portflio
        portfolio: dict = self.player.portfolio
        assert stock_name in portfolio.keys()
        assert portfolio[stock_name] >= quantity
        portfolio[stock_name] -= quantity

        # add transaction to market
        transaction: Transaction = Transaction(
            self.player, stock, quantity, total_sale, False)
        self.stock_market.transactions.append(transaction)

        print(f"Sold {quantity} shares of {stock_name}")


class EndTurn(Action):
    def __init__(self) -> None:
        self.name: str = "End Turn"
        self.end_turn = True

    def run(self) -> None:
        pass
