#Take an integer input and check if it’s even or odd.


number = int(input("Enter the number:  "))
if number % 2 == 0:
  print("Number is even")
else:
  print("number is odd")

# Take 3 numbers from user input and print the greatest.
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2st number: "))
n3 = int(input("Enter the 3st number: "))

# First 100 units: free

# Next 100 units (101–200): ₹5/unit

# Beyond 200: ₹10/unit Take input for units and calculate bill.




if(n1 > n2 and n1 > n3):
  print("number 1 is the greatest ")
elif(n2 > n1 and n2> n3):
  print("number 2 is the greatest")
else:
  print("number 3 is the greatest")


unit = int(input("Enter your eletric units:  "))

if(unit < 100):
  print("you have got free eletricity")
elif(unit>100 and unit<200):
  print(unit*5)
else:
  print(unit * 10)



