l=[6,2,3,4,5,6]
onlieven=filter(lambda x:x%2==0,l)
doubleeven=map(lambda x:x*2,onlieven)
sortt=sorted(doubleeven)
print(sortt)