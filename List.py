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

# Comprehension in python for above code
# Return a list of smaller element then the given element
def getSmaller(l,x):
    s = [i for i in l if i<x]
    return (s)

l=[10,20,3,4,5,6,22,111]
x= 10
r=getSmaller(l,x)
print(r)

# write own code to find largest no. in the list without using max function
# O(n^2)
def findLargest(l):
    for i in l:
        for j in l:
            if j>i:
             break
        else:
            return i
l = [1,2,3,4,5,6,1,10,2]
r=findLargest(l)
print (r)

#Above code in efficient manner

def getlargest(l):
    if not l:
        return None
    else:
        res=l[0]
        for i in range (1,len(l)):
            if l[i]>res:
                res=l[i]
        return res

# write own code to find second largest no. in the list 
def getSmax(l):
    if len(l)<=1:
        return None
    else:
        m= max(l)
        res=None
        for i in l:
            if i!=m:
                if res == None:
                    res=i
                else:
                    res = max(res,i)
        return (res)

l = [6,6,3,3]
r=getSmax(l)
print (r)