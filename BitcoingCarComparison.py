import csv

file = open('BTC-USD.csv')
csvreader = csv.reader(file)
header=[]
header =next(csvreader)
print(header)
results =[]

for row in csvreader:
    results.append(row)
results.pop(0)
print(results[0])
print()
bitcoinstash = 0
totalweeks = 0
for eachrow in results:
    price = (float((eachrow[2]))+float((eachrow[3])))/2
    bitcoinstash += 100/price
    totalweeks += 1
print(bitcoinstash)
totalInvested = totalweeks*100*1.28
currentvalue = bitcoinstash*float(results[-1][3])*1.28
print(totalInvested)
print(currentvalue)

print(len(results))
for i in range(39):
    results.pop(0)

print(len(results))
carbitcoinstash = 0
carweeks = 0
for n in results:
    price = (float((n[2]))+float((n[3])))/2
    carbitcoinstash += 117/price
    carweeks += 1
print(carbitcoinstash)
carinvested = totalweeks*117*1.28
carcurrentvalue = carbitcoinstash*float(results[-1][3])*1.28
print(carinvested)
print(carcurrentvalue)

couldhavebeen = carbitcoinstash*60000*1.28
print(couldhavebeen)




