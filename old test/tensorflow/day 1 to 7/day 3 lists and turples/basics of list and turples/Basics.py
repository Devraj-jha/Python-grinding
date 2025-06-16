my_list = [1,2,3,4,5] #this is a list it is mutualable 
print(my_list[0]) #can be used to access certain item of a list

#slicing means Skipping having a different value first and last etc
print(my_list[:3])
#list[start:end:skip]
#list methods
my_list.append(40) #list will add 40 in end
# Extend the list with multiple elements
my_list.extend([50, 60])
print(my_list)  # Output: [10, 99, 20, 30, 40, 50, 60]


#truples
a = (1,3,4,5,6,7) #once created can't be changed
#they cant be changed
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

#packing unpacking 
# Packing a tuple
my_tuple = (1, "apple", 3.14)

# Unpacking the tuple
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: apple
print(c)  # Output: 3.14
nested_tuple = ((1, 2), (3, 4), (5, 6))

# Accessing an element of the nested tuple
print(nested_tuple[1])  # Output: (3, 4)
print(nested_tuple[1][0])  # Output: 3

