PricesList_inr=[3000,56000,45000,2300]
def inrtousd():
    usd=map(lambda x:x*0.012,PricesList_inr)
    print(list(usd))
def inrtoeuro():
    euro=map(lambda x:x*0.011,PricesList_inr)
    print(list(euro))
inrtousd()
inrtoeuro()
