contact_book = {}
while True:
  print("\n---Contact book---")
  print("1. Add contact")
  print("2. remove contact")
  print("3. Display contact")
  print("4. Search Contact ")
  print("5. Exit")

  choice = input("Enter your choice:  ")
  if choice == "1":
    name = input("Enter Your Name:  ")
    phone_number = input("Enter your phone number:  ")
    contact_book[name] = phone_number
    print(f"{name}:{phone_number} added successfully")
  elif choice == "2":
    name = input("Enter your name:  ")
    if name in contact_book:
      del contact_book[name]
      print(f"{name} removed successfully")
    else:
      print("user not found")
  elif choice == "3":
    if contact_book:
      print("\n Contacts")
      for name,contact_book in contact_book.items():
        print(f"{name}: {contact_book}")
  elif choice == "4":
    name = input("Enter the name")
    if name in contact_book:
      print(f"{name}: {contact_book[name]}")
    else:
      print("Contact Not Found")

  elif choice =="5":
    print("Exiting....")
    break
  else:
    print("Invalid choice")
