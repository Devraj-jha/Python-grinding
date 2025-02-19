#Write a Python program using a while loop to print all the even numbers from 1 to 100.
i = 2
while i<= 100:
  print(i)
  i = i + 2
#Write a Python program using a for loop to print all the even numbers from 1 to 100.
for i in range(2,101,2):
  print(i)

for i in range(2,101):
  if i % 2 ==0:
    print(i)
  else:
    continue