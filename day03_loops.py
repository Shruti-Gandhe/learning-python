# Day 03: Loops in Python

# Example 1: for loop (printing numbers)
print("Example 1: For Loop")
for i in range(1, 6):
    print(i)

# Example 2: for loop with a list
print("\nExample 2: Loop through a list")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Example 3: while loop
print("\nExample 3: While Loop")
count = 1
while count <= 5:
    print(count)
    count += 1

# Example 4: break statement
print("\nExample 4: Break statement")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Example 5: continue statement
print("\nExample 5: Continue statement")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
