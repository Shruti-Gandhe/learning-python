# Day 02: Conditions in Python 

#Example 1: Voting Eligibility 
#This is an example of the "if-else condition"
name = input("Enter Your name:")
age = int(input("Enter your age:"))

if age>=18:
  message = "You are eligible to vote"
else:
  message = "You are not eligible to vote"
  
print(f"\nVoting Eligibility:\nName: {name}\nAge: {age}\n{message}")

#Example 2: Report Card 
#This is an example of the "if-elif-else condition"
name = input("Enter your Name: ")
subject = input("Enter subject name: ")
score = int(input(f"Enter your {subject} score: "))

if score>=90:
  grade = "A+"
elif score>=80:
  grade = "A-"
elif score>=75:
  grade = "B+"
elif score>=50:
  grade = "B-"
else:
  grade = "F"
  
print(f"""
===================
REPORT CARD 
Name: {name}
Subject: {subject}
Score: {score}
Grade: {grade}
===================
""")
