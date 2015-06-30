from decimal import *

getcontext().prec = 120
tot = 0
for i in range(2,100):
    num = Decimal(i).sqrt()
    num = str(num).replace(".","")
    if len(num) <100:
        continue
    num = num[:100]
    for x in num:
        tot+=int(x)
print tot
