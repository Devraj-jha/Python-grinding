a = [1,3,4,55,56,4,3,4,5,6,643]
a.sort() ## Sort the list in ascending order
print(a)
a.reverse #sort the list in descending order
print(a)
print(a.count(4)) # Count occurrences of 1
# Find the index of first occurrence of 4
print(a.index(4))  # Output: 2

# Create a shallow copy of the list
new_list = a.copy()
print(new_list)  # Output: [9, 5, 4, 3, 1, 1]