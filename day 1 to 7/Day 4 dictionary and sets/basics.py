# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
 #a dicitonary A dictionary is a collection of key-value pairs. Each key is unique and maps to a specific value
 
# Accessing a value using a key
name = my_dict["name"]
print(name)  # Output: Alice

del my_dict["city"]
print(my_dict)
# Using keys, values, and items methods
print(my_dict.keys())   # Output: dict_keys(['name', 'age'])
print(my_dict.values()) # Output: dict_values(['Alice', 30])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30)])

# Using get() to safely access values
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Not Found"))  # Output: Not Found
