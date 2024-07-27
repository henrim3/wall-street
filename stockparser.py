import random
from stock import Stock

bcproportion = 0.6     #the proportion blue chip stocks should have in the market... 0.6 = 60% 
penproportion = 0.4     #the proportion penny stocks should have in the market... 0.4 = 40% 

def addStocks(stocks, stockandtikrs, filename, marketsize, marketshares): 
    file1 = open(filename, 'r')
    bluechips = []
    pennies = []
    bluechipshares = marketshares * bcproportion
    pennyshares = marketshares * penproportion
    bluechipamt = marketsize//2
    pennyamt = marketsize//2 + marketsize%2
    for line in file1:
        info = line.split(',')
        price = info[2][1:]
        price = round(float(price), 2)
        if len(info[1]) > 60:
            continue
        if (price > 50 and price < 100) or (price > 1 and price < 5):
            risklvl = 1
            potreturn = 1
            marketinf = 1
            if price > 50 and price < 100:
                stockrep = bcproportion / bluechipamt
                shares = bluechipshares // bluechipamt
                mu = 0.07
                sigma = 0.15
                tmp = Stock(info[1],info[0],True,price,risklvl,potreturn, marketinf, stockrep, shares, mu, sigma)
                bluechips.append(tmp)
            else:
                stockrep = penproportion / pennyamt
                shares = pennyshares // pennyamt
                mu = 0.15
                sigma = 0.6
                tmp = Stock(info[1],info[0],False,price,risklvl,potreturn, marketinf, stockrep, shares, mu, sigma)
                pennies.append(tmp)
            stockandtikrs[info[0]] = tmp
    sbluechips = (random.sample(bluechips, bluechipamt))
    spennies = (random.sample(pennies, pennyamt))
    spennies.sort(key=lambda stock: stock.ticker)
    sbluechips.sort(key=lambda stock: stock.ticker)
    stocks.clear()
    stocks.extend(spennies)
    stocks.extend(sbluechips)
