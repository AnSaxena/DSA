# List introduction (put print command before the line to see the result)
l =[10,20,30,40,50]
(l)
(l[-4]) #using indexes to identify the number in a list.

# some python program with list
l.append(20) # will add 20 at the end of the list.
(l)

l.insert(1,15) # here the first element is the index number and the second is the number you wanted to add in a list.
(l)            #[10,15,20,30,40,50]

(15 in l) # will check whether the given number is present in the list and return boolean.( true/false)

(l.count(30)) # will give the total no. of count the number provided , i.e how many times it appears in the list.

(l.index(30))#[10,15,20,30,40,50], to check the index number of the given no.

#(l.index(30,4,7)) # calling index function with two more parameters, start index(inclusive) and end index(exclusive)  

#python program to understand removal of elements.

l =[10,20,30,40,50,60,70]
l.remove(20)
(l)

print(l.pop())# remove the item from the end of the list.
(l)      

print(l.pop(3)) # remove the item acc to the indexes
print(l)     

del l[1] #delete the element at index 1 of the list
print(l)

del l[0:2] # remove data with in a range
print (l)

