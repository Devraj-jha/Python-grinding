my_list = [10, 20, 30, 40]

# Remove a specific element (first occurrence)
my_list.remove(20)
print(my_list)  # Output: [10, 30, 40]

# Pop the last element (default)
removed_element = my_list.pop()
print(removed_element)  # Output: 40
print(my_list)          # Output: [10, 30]

# Clear all elements
my_list.clear()
print(my_list)  # Output: []
