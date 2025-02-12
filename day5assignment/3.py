# You have sales data for different regions and want to calculate the total sales for each region.

sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
total_sales_data={}
for i in sales_data:
    if i["region"] not in total_sales_data:
        total_sales_data[i['region']]=i["sales"]
    else:
        total_sales_data[i["region"]]+=i["sales"]
print(total_sales_data)