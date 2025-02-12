products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]

sortedbyprice=sorted(products,key=lambda x:(x['price'],x['name']))
print(sortedbyprice)