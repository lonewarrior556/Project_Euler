import math
import decimal
decimal.getcontext().prec=30

d=dict()

bot=decimal.Decimal(1)/decimal.Decimal(3)
top=decimal.Decimal('.5')

for x in range(3,12000):
    print x
    for y in range((x)/3,int(math.ceil((0.5)*x))):
        temp= decimal.Decimal(y)/decimal.Decimal(x)
        if temp>bot and temp<top:
            d[temp]=1            

            











print len(d)
