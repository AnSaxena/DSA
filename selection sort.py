def selectSort(l): 
    n= len(l)
    for i in range(n-1): 
        min_ind = i # initializing the min index as i
        for j in range (i+1, n):
            if l[j]<l[min_ind]:
                min_ind = j
        l[min_ind],l[i] = l[i],l[min_ind]
    print(l)
    return 0

list= [1,5,2,9,1,7]
selectSort(list)

        #for this we will iterate loop for n-2 times 
        # (0, n-2) as if the size of a list is 5 we 
        # run loop for 4 but in selection sort where 
        # we do not perform iteration at last element 
        # as it is itself is a largest and smallest no. 
        # in an array coz it it the only element. So, 
        # we will run from (0 , n-2) times so to get 
        # this in our range we will run n-1.