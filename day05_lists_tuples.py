#Day 05 Lists and Tuples 
#Example 01 
marks = [85, 90, 74, 65]
print("Marks: ", marks)

marks.append(90)
print("Updated Marks: ", marks)

#Exampl 02 
total = sume(marks)
average = total / len(marks)

print(f"Total Marks: {total}")
print(f"Average Marks: {average}")

#Example 03
print("\n Marks Status: ")
for mark in marks;
  if marks >= 40:
    print(marks, "--> Pass")
  else:
    print(marks, "--> Fail")

#Example 04
subjects = ["Maths", "Science", "Geography"]
print("\nSubjects: ", subjects)

for subject in subjects:
  print("Subject: ", subject)



#Example 05
print("First Subject: ", subjects[0])
print("Last marks: ", marks[-1])

#Example 06: Shopping Cart
cart[]
n = int(input(" Enter number of Items: "))

for i in range(n):                                     #push values are not used in python i++ or i>= 
  cost = input("Enter Cost of Items: "))
  cart.append(cost)

print("Shopping Cart Items: ", cart)
print("Total: ", sum(cart))

#Example 07: Attendance List
students = ["Shruti" ,"Maya" ,"Aarav" ,"Meera"]
students.append("Riya")
students.remove("Meera")

print("\nUpdated Students Attendance List: ",students)
for student in students:
  print(student)

#another example 
students = []
n = int(input("Enter number of Students: "))

for i in range(n):
  names = input("Enter Students Names: ")
  students.append(names)

print("\n Students Attendance: ", students)
for student in students:
  print(student)
  
print("Total Students: ", len(students))

#Example 08: Weeks 
days = ["Monday", "Tuesday" , "Wednesday" , "Thrusday" , "Friday" , "Saturday" , "Sunday"]
print("Weekends: ", days[5:])

#another example 
days = []
for i in range(7):
  day = input("Enter day {i+1}: ")
  days.append(day)
print("Weekends: ", day[5:])
