def insertionSort(l):
    for i in range (1,len(l)):
        x=l[i] #we gonna store the current element l[i] and put it at its correct position.
        
        j=i-1 #consider element just before current element
        
        while j>=0 and x<l[j]:# we gonna move towards the 0 index and check
            l[j+1]=l[j] #once we move towards left side if the elements is greater than current element we move it ahead.
            
            j = j-1
            
        l[j+1]=x

    print ("final result", l)
    return 0
    
l = [1,8,3,9,2,4]
insertionSort(l)