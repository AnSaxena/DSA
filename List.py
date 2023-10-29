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
def sLarger(l):
    if len(l)<=1:
        return None
    m= max(l)
    s=None
    for i in l:
        if i!=m:
            if s == None:
                s=i
            else:
                s=max(s,i)
    return s

#Checking whether the list is sorted or not   
l = [4, 4]
res = sLarger(l)
print(res)

def isSorted(l):
    if len(l)<= 1:
        return True
    else:
        for i in range(len(l)-1):
            if l[i]<=l[i+1]:
                i=i+1
            else:
                return False
        return True
                
l=[1,4,1,1,2]
e=isSorted(l)
print(e)


#Using Sorted function for above code
def isSorted(l):
    sl= sorted(l)
    if sl = l:
        return True
    else:
        return False
