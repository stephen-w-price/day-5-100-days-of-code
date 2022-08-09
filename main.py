# Loops

# For loop

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

print("---average student height---")

student_heights = input("Input a list of student heights ").split(', ')
n = 0
total = 0
for student_height in student_heights:
    student_height = int(student_height)
    n += 1
    total += student_height
    print(n)
    print(total)

print(f"this is the total: {total} and this is the number of students: {n}")
average = total / n 

print(f"this is the average height of students {average}")

