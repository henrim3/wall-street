import csv
from stock import Stock

def addStocks(stocks, stockandsymbols, filename):
    file1 = open(filename, 'r')
    for line in file1:
        info = line.split(',')
        price = info[2][1:]
        price = round(float(price), 2)
        risklvl = 1
        potreturn = 1
        tmp = Stock(info[1],info[0],price,risklvl,potreturn)
        stocks.append(tmp)
        stockandsymbols[info[0]] = tmp