# Day 02: Conditions in Python 

#Example 1
#This is an example of the "if-else condition"
name= "Shruti"
age= 19

if age>=18:
  message = "You are eligible to vote"
else:
  message = "You are not eligible to vote"
  
print(f"Name: {name}\nAge: {age}\n{message}")

#Example 2 
#This is an example of the "if-elif-else condition"
name = "John"
score = 75

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
  
print(f"Name: {name}\nScore: {score}\nGrade: {grade}")
