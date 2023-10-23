# a=[10,15,20]
# b = [5,6,6,30]

# expecting output res=[5,6,6,10,15,20,30]

#-----------------------------------------

#knife solution
def mergeSort(a,b):
    res=a+b
    res.sort()
    return res

a=[1,4,2]
b=[1,5,9]
result=mergeSort(a,b)
print (result)

#Time complexity:
#(m+n)*log(m+n) as m-> len(a) and n-> len (b)
#this is not sufficient

#---------------------------------------------

def merge_sort(m,n):
    res=[]
    q=len[m]
    r=len[n]
    


