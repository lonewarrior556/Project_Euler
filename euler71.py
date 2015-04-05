import math
import decimal 
decimal.getcontext().prec=40

ans=decimal.Decimal('0.4285712857138571415714247142741428224285')

ls=[]
for x in range(3,1000001):
    for y in range((3*x)/7,int(math.ceil((3./7)*x))):
       # ls.append(decimal.Decimal(y)/decimal.Decimal(x))
        if decimal.Decimal(y)/decimal.Decimal(x)==ans:
            print y,x
            
ls=set(ls)
ls=list(ls)
ls.sort()


        
