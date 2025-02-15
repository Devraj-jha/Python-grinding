"""Write a Python program that takes a string input from the user and prints:

The first 3 characters of the string.
The last 3 characters of the string.
A slice that contains the middle part of the string (excluding the first and last character)."""

a = str(input("Enter your Text: "))
print(a[:3])
print(a[3:])
print(a[1:-1])
