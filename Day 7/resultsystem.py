name = input("Enter student name: ")

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)

if marks1 < 40 or marks2 < 40 or marks3 < 40:
    print("Result: Fail")

elif average >= 90:
    print("Result: Outstanding")

elif average >= 75:
    print("Result: Distinction")

elif average >= 60:
    print("Result: First Class")

elif average >= 50:
    print("Result: Second Class")

else:
    print("Result: Pass")