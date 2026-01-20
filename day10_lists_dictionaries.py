students = []

for i in range(3):  # Add 3 students
    student = {}  # dictionary for each student
    
    student["name"] = input("Enter student name: ")
    student["roll_no"] = input("Enter roll number: ")
    student["score"] = int(input("Enter score: "))
    
    # Assign grade
    if student["score"] >= 90:
        student["grade"] = "A+"
    elif student["score"] >= 80:
        student["grade"] = "A"
    elif student["score"] >= 70:
        student["grade"] = "B+"
    else:
        student["grade"] = "C"
    
    students.append(student)  # Add this dictionary to the list


print("\n--- ALL STUDENT REPORTS ---")
for student in students:
    print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Score: {student['score']}, Grade: {student['grade']}")


with open("students_db.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")


top_student = max(students, key=lambda x: x["score"])
print("\nTop Student:")
print(top_student)

