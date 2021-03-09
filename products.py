products = []
while True:
	name = input('input product name: ')
	if name =='q':  #如果使用者输入q,就结束这个循环
		break
	price = input('input price: ')
	products.append([name,price])
print(products)

for p in products:
	print("the price of ",p[0]," is ",p[1])
