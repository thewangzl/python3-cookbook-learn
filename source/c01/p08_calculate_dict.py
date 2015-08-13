#

'''
Topic:字典的运算
'''

def calc_dict():
	prices = {
		'ACME':45.23,
		'AAPL':612.78,
		'IBM':205.55,
		'FB':10.75
	}

	min_price = min(zip(prices.values(),prices.keys()))
	max_price = max(zip(prices.values(),prices.keys()))
	print('min_price is' , min_price)
	print('max_price is', max_price)
	
	prices_sorted = sorted(zip(prices.values(),prices.keys()))
	print('prices_sorted is' , prices_sorted)
	
	prices_and_names = zip(prices.values(), prices.keys())
	print(min(prices_and_names))

	print(min(prices))
	print(max(prices))

	min(prices, key=lambda k:prices[k])
	max(prices, key=lambda k:prices[k])

	min_value = prices[min(prices,key=lambda k: prices[k])]

	prices = {'AAA' : 45.23, 'ZZZ' : 45.23}
	print(min(zip(prices.values(),prices.keys())))
	print(max(zip(prices.values(),prices.keys())))

if __name__ == '__main__':
	calc_dict()


