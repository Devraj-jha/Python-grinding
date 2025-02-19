#Ask user to input his age and print his eligibility



a = int(input("Enter your age:  "))
is_eligible = input("are you a citizen of india(yes/no):  ").lower() == "yes"

if a>0 and a <18 :
  print("you are minor")
elif a >=18 and a<100 and is_eligible:
  print("your are eligible")
else:
  print("your are not eligible")