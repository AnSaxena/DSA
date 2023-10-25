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

# Comprehension in python for above code
def evenOdd(l):
    e= [i for i in l if i%2==0]
    o= [i for i in l if i%2!=0]
    return (e,o)

l=[10,11,12,13]
r=evenOdd(l)
print (r) 


# Return a list of smaller element then the given element
def getSmaller (l,x):
    s=[]
    for i in l:
        if i<x:
            s.append(i)
    return(s)

l=[10,20,30,40]    
x=30
r=getSmaller (l,x)
print(r)