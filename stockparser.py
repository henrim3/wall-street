import csv
import random
from stock import Stock

def addStocks(stocks, stockandtikrs, filename, marketsize):
    file1 = open(filename, 'r')
    bluechips = []
    pennies = []
    for line in file1:
        info = line.split(',')
        price = info[2][1:]
        price = round(float(price), 2)
        if (price > 50 and price < 100) or (price > 1 and price < 5):
            marketcap = 0.01
            risklvl = 1
            potreturn = 1
            marketinf = 1
            if price > 50 and price < 100:
                needed = 2000
                mu = 0.07
                sigma = 0.15
                tmp = Stock(info[1],info[0],price,risklvl,potreturn, marketinf, marketcap, needed, mu, sigma)
                bluechips.append(tmp)
            else:
                needed = 10000
                mu = 0.15
                sigma = 0.6
                tmp = Stock(info[1],info[0],price,risklvl,potreturn, marketinf, marketcap, needed, mu, sigma)
                pennies.append(tmp)
            stockandtikrs[info[0]] = tmp
    sbluechips = random.sample(bluechips, marketsize//2)
    remaining = marketsize//2
    if marketsize % 2 == 1:
        remaining += 1
    spennies = random.sample(pennies, remaining)
    stocks.clear()
    stocks.extend(sbluechips)
    stocks.extend(spennies)
    random.shuffle(stocks)