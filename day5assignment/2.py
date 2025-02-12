# Store management
   
initial_stock = {"apple": 50,"banana": 100,"orange": 75}

sold_item = {"apple": 10, "banana": 20, "orange": 15}

#   calculate the current stock and display current stock

# init=int(initial_stock.values())
# sold=int(sold_item.values())
current={}
for i in initial_stock:
    current[i]=initial_stock[i]-sold_item[i]

print(current)







