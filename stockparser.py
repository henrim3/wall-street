import csv
import random
from stock import Stock

def addStocks(stocks, stockandtikrs, filename, marketsize):
    file1 = open(filename, 'r')
    totstocks = []
    for line in file1:
        info = line.split(',')
        price = info[2][1:]
        price = round(float(price), 2)
        risklvl = 1
        potreturn = 1
        marketinf = 1
        tmp = Stock(info[1],info[0],price,risklvl,potreturn, marketinf)
        totstocks.append(tmp)
        stockandtikrs[info[0]] = tmp
    selectedstocks = random.sample(totstocks, marketsize)
    stocks.clear()
    stocks.extend(selectedstocks)