#Day 04 
#Its an alternative example of the simple calculator using the menu driven method.

def show_menu():
  print("\n 1. Addition")
  print("2. Subtraction")
  print("3. Multiply")
  print("4. Exit")

while True:
  show_menu():
  choice = input("Enter Choice: ")
      if choice == "4":
        print("Exiting Program")
        break

a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))

 if choice == "1":
   print("Result: ", calculate(a, b, "add"))
 elif choice == "2":
   print("Result: ", calculate(a, b, "sub"))
elif choice == "3":
   print("Result: ", calculate(a, b, "mul"))
else:
   print("Invalid choice")


#This is ATM program 
def show_atm_menu():
  print("\n 1. Check Balance")
  print("2. Withdraw")
  print("3. Exit")

while True:
  show_atm_menu():
choice = input("Enter Choice: ")

   if choice == "3":
     print("Goodbye!!! Have a Good Day.")
     break

#This is Login Program
while True:
  password = input("Enter password: ")

if password == "admin@123":
   print("Login Successfully!!!")
else:
   print("Invalid password. Try Again!!")
