#Day 07 
#Example 01 
numbers = {1, 2, 3, 4, 4, 5}
print("Numbers: ", numbers)

#Example 02 
marks = {90, 78, 65, 89, 80, 50, 90}
unique_marks = set(marks)
print("\n Unique Marks: ", unique_marks)

#Example 03
subjects = {"Maths", "Science", "English", "Geography"}
subjects.add("Computer")
subjects.remove("Geography")

print("Subject Names: ", subjects)

#Example 04
class_A = {"Shruti", "Maya", "Aarav", "Rohan"}
class_B = {"Karan", "John", "Riya", "Aarav"}

print("\nUnion: ", class_A | class_B)
print("Insertion: ", class_A & class_B)
print("Difference (A - B): ", class_A - class_B)

#example 05
registrations = set()

while True:
    name = input("Enter participant name (or 'exit'): ")

    if name.lower() == "exit":
        break

    registrations.add(name)

print("\nRegistered participants:")
for participant in registrations:
    print(participant)

#Example 06
student1_subjects = {"Math", "Science", "English"}
student2_subjects = {"Science", "Computer", "English"}

common_subjects = student1_subjects & student2_subjects
print("\nCommon Subjects:", common_subjects)
