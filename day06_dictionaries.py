#Day 06
#Example 01
student = {
  "name" : "Shruti"
  "age" : 19
  "branch" : "AIML"
}
print("Student Name: ", student["name"])
print("Student Age: ", student["age"])
print("Student Branch: ", student["branch"])

#Example 02
users = {
    "shruti": "1234",
    "admin": "admin123"
}

username = input("\nEnter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid credentials")

#Example 03
report_card = {
    "Name": "John",
    "Math": 88,
    "Science": 92,
    "English": 75
}

print("\nREPORT CARD")
for key, value in report_card.items():
    print(f"{key}: {value}")

#Example 05
total = sum(marks.values())
average = total / len(marks)
print("Average Marks:", average)
