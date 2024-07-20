Changes:

-Created "Stock" Class
	-holds name, symbol, price, risklvl (risk level), potreturn (potential return), (marketinf), market influence
	-Stock class has fluctuate function, to be implemented

-Stock Market
	- Reads in stock info from input file, Large file in data (source: https://www.nasdaq.com/market-activity/stocks/screener?exchange=NASDAQ&render=download")... 
		-will work with any stock following the form, "symbol, name, $price, blahblahblah, blahblah,..."
			-i.e. "ZYXI,Zynex Inc. Common Stock,$9.29,-0.31,-3.229%,295191450.00,United States,,66599"
			-Note $ must be included
			-undefined behavior when not following that format
		-Uses stockparser to parse file for stock info
	- Stores stocks as a list of objects
	- Stores the name of the stock, as well as its object in a dictionary, allowing easy access
	- get_stock(symbol) returns the stock object corresponding to the symbol

-Player, Game
	- Minor changes to account for using stock objects now
	- asks for symbol when buying stock rather than name <=== We can change this back

To do:
	- Implement stock fluctuations
	- Implement other assets... need a new market?
	- Implement a way to distinguish between golden opportunity stocks
	- Create a smaller .txt file of stocks