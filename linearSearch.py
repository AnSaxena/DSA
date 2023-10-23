def linear_search(my_list, key):
    for i in range(0, len(my_list)):
        if my_list[i] == key:
            return i

    return -1
#-------------------------------








list= input("Enter a list")
key = input("Enter a key")
my_list = list.split()
ls=linear_search(my_list,key)
print (ls)