# e = 2+1/(1+1/(2+1/(1+1/(1+1/(4+.....))))))




def makestring(limit):
    beg="2+1/"
    c=2
    for i in range(limit):
        beg+="(1+1/("+str(c)+"+1/(1+1/"
        c+=2
    beg+='(1+1/'+str(c)    
    return beg

def eval_last(string):
    if not '(' in string:
        a=string.find('/')
        top=int(string[a+1:])*int(string[0])+int(string[2:a])
        return str(top)+'/'+string[a+1:]
    a=string.rfind('+')
    b=string.rfind("/")
    den=int(string[b+1:])
    c=string.rfind('/(')
    d=string.rfind('+')
    num=int(string[a+1:b])+int(string[c+2:d])*den
    string=string[:c]
    string=string[:string.rfind('+')+1]
    return eval_last(string+str(den)+'/'+str(num))
    
