#Day 09
#Dictionarries + other Methods 

#Student report card
student = {}

student["name"] = input("Enter name: ")
student["roll_no"] = input("Enter roll number: ")
student["score"] = int(input("Enter score: "))

if student["score"] >= 90:
    student["grade"] = "A+"
elif student["score"] >= 80:
    student["grade"] = "A"
elif student["score"] >= 70:
    student["grade"] = "B"
else:
    student["grade"] = "C"

print("\n--- STUDENT REPORT ---")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

#Dictionary + file handling
with open("students.txt", "a") as file:
    file.write(str(student) + "\n")

#Login Data 
user = {
    "username": input("Username: "),
    "password": input("Password: ")
}
print("Login data saved")

#PhoneBook
phonebook = {}
phonebook["Shruti"] = "9876543210"
phonebook["Aarav"] = "9123456789"

print(phonebook)
