startdate=[1,1,1900,1]


# if statements..
def nextday(date,n):
    if date[3]==7 and date[1]==1:
        n+=1
    
    if date[1]== 30 and date[0] in [4,6,9,11]:
        date[0]=date[0]+1
        date[1]=1
  #      if date[3]==7:
  #          date[3]=1
  #      else:date[3]=date[3]+1
    elif date[1]== 31 and date[0] in [1,3,5,7,8,10,12]:
        if date[0]==12:
            date[0]=1
            date[1]=1
            date[2]=date[2]+1
        else:
            date[0]=date[0]+1
            date[1]=1
 #       if date[3]==7:
 #           date[3]=1
 #       else:date[3]=date[3]+1
    elif date[0]==2 and date[1] in [28,29]:
        if date[1]==29:
            date[0]=3
            date[1]=1
        elif date[2]%4==0 and date[2]!=1900:
            date[1]=29
        else: 
            date[1]=1
            date[0]=3
 #       if date[3]==7:
 #           date[3]=1
 #       else: date[3]=date[3]+1
    else: 
        date[1]=date[1]+1
    if date[3]==7:
        date[3]=1
    else: date[3]=date[3]+1
    return date, n

