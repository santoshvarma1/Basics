import csv
file = open('BTC-USD-1.csv')
reader = csv.reader(file)


all = []
for each in reader:
    all.append(each)

print(all.pop(0))

bitcoinstash = 0
totaldays = 0

for every in all:
    dailystash = 10 / float(every[2])
    bitcoinstash+=dailystash
    totaldays += 1

print(f'total money invested is {totaldays*10}')
print(f'total bitcoin accrued {bitcoinstash}')
print(f'current networth is {bitcoinstash*float(all[-1][2])}')
print(f'networth when it was at peak{bitcoinstash*60000}')
