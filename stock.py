import numpy as np

class Stock:
    def __init__(self, name="", ticker="", isbluechip= False, price=0, risklvl=0, potreturn=0, marketinf=0, stockrep=0.01, shares=10000, mu=0.1, sigma=0.2, dt=5/252):
        self.name = name
        self.ticker = ticker
        self.isbluechip = isbluechip
        self.price = price
        self.risklvl = risklvl
        self.potreturn = potreturn
        self.marketinf = marketinf
        self.start = price
        self.totchange = 0
        self.change = 0
        self.mu = mu        # Drift coefficient
        self.sigma = sigma  # Volatility coefficient
        self.dt = dt        # Time increment
        self.owned = 0
        self.shares = shares    #shares available 
        self.needed = shares //2 + shares %2  #shares needed for stock to be under a players management 
        self.stockrep = stockrep      #The proportion of the total market that the stock represents 0.06 -> 6%
        self.is_recession = True  # Default condition

    def fluctuate(self):
        tmp = self.price
        # Generate a random number from a standard normal distribution
        W = np.random.standard_normal()

        # Adjust mu and sigma based on market condition
        if self.is_recession:
            mu_adjusted =  - 0.2  # Decrease the drift coefficient during recession
            sigma_adjusted = 0.5  # Increase the volatility during recession
        else:
            mu_adjusted = self.mu
            sigma_adjusted = self.sigma

        # Update the stock price using GBM formula
        self.price = self.price * \
            np.exp((mu_adjusted - 0.5 * sigma_adjusted**2) *
                   self.dt + sigma_adjusted * np.sqrt(self.dt) * W)
        self.change = self.price - tmp
        self.price = self.price * np.exp((self.mu - 0.5 * self.sigma**2) * self.dt + self.sigma * np.sqrt(self.dt) * W)
        self.change = ((self.price - tmp)/tmp) * 100
        self.totchange = ((self.price - self.start)/self.start) * 100
        self.price = round(float(self.price), 2)
        print(f"Stock {self.ticker} fluctuated from {tmp:.2f} to {self.price:.2f}")

    def printinfo(self):
        print(f"\nName: {self.name}")
        print(f"Ticker: {self.ticker}")
        print(f"Price: {self.price:.2f}")
        print(f"Daily Change: {self.change:.2f}%")
        print(f"Total Net Change: {self.totchange:.2f}%")
        print(f"Current Shares Owned: {self.owned}")
        print(f"Market Capitalization: {int(self.shares)}")
        print(f"Stock Representation: {round(self.stockrep * 100,2) }%")

    def set_market_condition(self, condition: str):
        """ Set the market condition.
            Args:
                condition (str): The market condition ('normal' or 'recession').
        """
        if condition == 'recession':
            self.is_recession = True
            print(f"{self.name} is now in a recession.")
        else:
            self.is_recession = False
            print(f"{self.name} is now in a normal market condition.")
