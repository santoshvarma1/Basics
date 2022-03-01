import csv

file = open('TSLA.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)


results = []
for each in csvreader:
    results.append(each)


totalStash = 0
totalWeeks = 0
for row in results:
    priceOfWeek = (float(row[2])+float(row[3]))/2
    StockPurchasedPerWeek = 100/priceOfWeek
    totalStash = totalStash + StockPurchasedPerWeek
    if row == results[-1]:
        print(f'current value of the stock is at {totalStash*priceOfWeek*1.28} cad')
        print(f'total weeks {totalWeeks}: and total investment at {totalWeeks*100}')
    totalWeeks += 1


