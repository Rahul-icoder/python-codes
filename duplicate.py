prices = [22,65,76,65,88,22,68,22]


print(len(prices))
print(prices.count(22))
print(prices[3:-1])

dupprices = []
for price in prices:
	if price not in dupprices:
		dupprices.append(price)
print(dupprices);