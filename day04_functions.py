#Day 04 : Funtions 
#Using Funtions and variables and parameters, etc.

#Example 01:
def greet():
print("Hello!! GitHub")
greet()

#Example 02:
def greet_user(name):
  print(f"\nHello!! Welcome to my GitHub, {name.capitalize()}!!")
greet_user(input(f"Enter Username: "))

#Example 03:
def add_numbers(a, b):
  return a + b
a = int(input(f"Enter the number: {a}"))
b = int(input(f"Enter the number: {b}"))

result = add_numbers(a, b):
print(f"Sum: {result}")

#Example 04:
def voting_eligibility(age):
  if age>=18:
    return "Eligible for voying"
  else:
    return "Not Eligible for voting"
  age = int(input("Enter your Age:"))
  print(voting_eligibilty{age})

#Example 05:
def calculate_grades(score):
  if score>=90:
    return "A+"
  elif score>=80:
    return "A-"
  elif score>=70:
    return "B+"
  elif score>=60:
    return "B-"
  elif score>=50:
    return "C+"
  else:
    return "Need to Improve!!!"
    
score = int(input(f"Enter your Score: "))
print(f"Grade: {calculate_grades(score)}")

#Example 06:
def simple_calculator(a, b, operation):
  if operation == "add":
    return a + b
  elif operation == "sub":
    return a - b
  elif operation == "mul":
    return a * b
  elif operation == "div":
        if b != 0:
          return a / b
        else:
          return "Cannot be divided by Zero"
  else:
    return "Invalid operation"

a = int(input(f"Enter the First Value: "))
b = int(input(f"Enter the Second Value: "))
operation = input("Enter type of operation (add/sub/mul/div): ").lower()

result = simple_calculator(a, b, operation)
print(f"Result: {result}")
