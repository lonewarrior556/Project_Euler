



# def count(limit):
#     1+1/2
    

#     1 + 1/(2+ 1/2)= 

    
#     1 + 1/(2 + 1/(2 + 1/2)=


#     1 + 1/(2 + 1/(2 + 1/(2 + 1/2)=



#     (2 + 1/2) = 5/2
    

#     (2 + 1/(5/2)) = (2 + 2/5)  = 12/5


#     (2 + 1/(12/5)) = (2 + 5/12)  = 29/12


def makestring(limit):
    limit=limit-1
    beg="1 + 1/"
    term="(2 + 1/"
    end="2"
    string= beg+(term*limit)+end
    string=string.replace('(2 + 1/2','(5/2')
    return string

def eval_last(string):
    a=string.rfind("(")
    b=string.rfind("/")
    den=int(string[b+1:])
    num=int(string[a+1:b])
    if a==6:
        numf=num+den
        if len(str(numf))>len(str(num)):
            return True
        else:
            return False
        
    else:
        numf=2*num+den
        term=str(numf)+'/'+str(num)
        return eval_last(string[:a-6]+term)
    
    
                  
def count():
    n=0
    for i in range(2,1001):
        s=makestring(i)
        if eval_last(s):
            n+=1
    return n
