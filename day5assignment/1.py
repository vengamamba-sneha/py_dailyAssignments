# calculate count the item frequency from the below products and store it in dictionary
products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
sepprod=products.split()
print(sepprod)
count={}
for i in sepprod:
    if i  in count:
        count[i]+=1
    else:
        count[i]=1
print(count)







