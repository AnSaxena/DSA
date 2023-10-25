#Check the odd and even number in list and seperate them
def evenOdd(l):
    e=[]
    o=[]
    for i in l:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    return e,o
    
l=[10,23,30,49]
r=evenOdd(l)
print (r)