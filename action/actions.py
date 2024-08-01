from action import Action
from player import Player
from stock import Stock
from stock_market import StockMarket


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

        # decrease player capital
        stock: Stock = self.stock_market.get_stock(stock_ticker)
        assert stock is not None
        total_price: int = stock.price * quantity
        assert self.player.capital >= total_price
        self.player.capital -= total_price
        stock.owned += quantity
        portfolio: dict = self.player.portfolio

        # add stock to portfolio if doesn't already exist
        if stock_ticker not in portfolio.keys():
            portfolio[stock_ticker] = 0

        # add stock to portfolio
        portfolio[stock_ticker] += quantity

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
        print(f"{self.player.name}'s Current Balance: ${self.player.capital:.2f}")


class GetStockInfo(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Get Stock Information"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:
        stock = self.player.choose_get_info(self.stock_market)
        stock.printinfo()


class SellStock(Action):
    def __init__(self, player: Player, stock_market: StockMarket) -> None:
        self.name: str = "Sell Stock"
        self.player: Player = player
        self.stock_market: StockMarket = stock_market

    def run(self) -> None:

        if (self.player.choose_sell_stock(self.stock_market) is None):
            print("CHOOSE SELL STOCK RETURNS NONE")
            return

        stock_name, quantity = self.player.choose_sell_stock(self.stock_market)

        # increase player capital
        stock: Stock = self.stock_market.get_stock(stock_name)
        assert stock is not None
        market_value: int = stock.price
        total_sale: int = market_value * quantity
        self.player.capital += total_sale

        # remove from portflio
        portfolio: dict = self.player.portfolio
        assert stock_name in portfolio.keys()
        assert portfolio[stock_name] >= quantity
        portfolio[stock_name] -= quantity

        print(f"Sold {quantity} shares of {stock_name}")


class EndTurn(Action):
    def __init__(self) -> None:
        self.name: str = "End Turn"
        self.end_turn = True

    def run(self) -> None:
        pass
