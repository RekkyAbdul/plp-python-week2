# exploring list data structure
# creating empty list
my_list = []

# assigning values to my_list
my_list = [10, 20, 30, 40]

# insert 15 to the second position in the list
my_list.insert(1, 15)
print(my_list)

# extending my_list values with list2
list2 = [50,60,70]
my_list.extend(list2)
print(my_list)

# delete the last element in my_list
del my_list[-1]
print(my_list)

# sorting list in ascending order
my_list.sort()
print(my_list)

# get the index value of 30 in my_list
mdex =  my_list.index(30)
print("the index of 30 in my_list is :", mdex)
