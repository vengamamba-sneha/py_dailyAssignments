products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]

price100=list(filter(lambda x:x['price']>100,products))
print(list(price100))
discount20=map(lambda x:{ "price":x['price']*0.8},price100)
print(list(discount20))

