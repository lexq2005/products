import OS    #OS is operating system

products = []
if os.path.isfile('product.xls'):   #通常用完全路径比较好
	print("Found File")
	with open('products.xls','r') as f:
	    for line in f:
		    if 'Product,Price' in line:
			    continue
		    name, price = line.strip().split(',') 
		    products.append([name, price])
    print(products)
else:
	print("File is Not Found")
 















