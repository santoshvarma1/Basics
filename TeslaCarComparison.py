import csv

file = open('TSLA.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)


results = []
for each in csvreader:
    results.append(each)


print(results)
print(header)

totalStash = 0
totalWeeks = 0
for row in results:
    print(row)
    priceOfWeek = (float(row[2])+float(row[3]))/2
    StockPurchasedPerWeek = 100/priceOfWeek
    totalStash = totalStash + StockPurchasedPerWeek
    print(f'purched stock this week {StockPurchasedPerWeek}, totalling stash at {totalStash}')
    if row == results[-1]:
        print(f'current value of the stock is at {totalStash*priceOfWeek*1.28} cad')
        print(f'total weeks {totalWeeks}: and total investment at {totalWeeks*100}')
    totalWeeks += 1

