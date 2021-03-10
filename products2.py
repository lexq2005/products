products = []
with open('products.xls','r') as f:
	for line in f:
		if 'Product,Price' in line:
			continue
		name, price = line.strip().split(',') 
		products.append([name, price])
print(products)





