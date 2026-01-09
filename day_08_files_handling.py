#Day 08

#Opening  a file.
file = open("filename.txt", "mode")
###Modes
#"r" → read
#"w" → write (overwrites)
#"a" → append (adds)
#"x" → create new file
#"r+" → read + write

#writing to a file.
name = input("Enter your name: ")

file = open("data.txt", "w")
file.write(name)
file.close()

print("Data saved successfully!")

#Reading to file
file = open("data.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)

#Appending to file.
file = open("data.txt", "a")
file.write("\nNew line added")
file.close()

#Mini Example
#Attendance File
name = input("Enter student name: ")

with open("attendance.txt", "a") as file:
    file.write(name + "\n")

print("Attendance marked!")

#Reading Attendance
with open("attendance.txt", "r") as file:
    print(file.read())
