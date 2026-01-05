#Day 03 Loops Condition
#example 1
print("\n Example 1 Student Attendance")
students = ["Shruti", "Meera", "Aarav", "Arjun"]
for student in students:
   print("f{students} is present ")


#Example 2
print("\nExample 2: Login Attempts")
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "admin123":
        print("Login successful")
        break
    else:
        attempts -= 1
        print(f"Wrong password. Attempts left: {attempts}")
if attempts == 0:
    print("Account locked")


#Example 3
print("\nExample 3: Shopping Cart")
prices = [int(input("Enter prices of the Items:"))]
total = 0
for price in prices:
    total += price
print("Total bill amount:", total)


#Example 4
print("\nExample 4: OTP Verification")
otp = "4321"
tries = 3
while tries > 0:
    entered = input("Enter OTP: ")
    if entered == otp:
        print("OTP Verified")
        break
    else:
        tries -= 1
        print("Incorrect OTP")
if tries == 0:
    print("OTP expired")


#Example 5
print("\nExample 5: Menu System")
while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Balance: ₹5000")
    elif choice == "2":
        amount = int(input("Enter amount: "))
        print(f"₹{amount} deposited")
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
