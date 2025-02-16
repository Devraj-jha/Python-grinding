# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 2, 4, 5}
