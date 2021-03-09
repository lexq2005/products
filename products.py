products = []
while True:
	name = input('input product name: ')
	if name =='q':  #如果使用者输入q,就结束这个循环
		break
	price = input('input price: ')
	products.append([name,price])
print(products)

print(products[0][0])
print(products[1][1])


