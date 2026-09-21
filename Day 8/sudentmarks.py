name = input("Enter student name: ")
m1 = float(input("Enter marks for subject 1:"))
m2 = float(input("Enter marks for subject 2:"))
m3 = float(input("Enter marks for subject 3:"))
total=m1+m2+m3
average = total/3

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)

if m1 < 40 or m2 < 40 or m3 < 40:
    print("Result:Fail")
elif average >= 90:
    print("Result: Outstanding")
elif average >= 80:
    print("Result: distinction")
elif average >= 60:
    print("Result: First Class")
elif average >= 50:
    print("Result: Second Class")
else:
    print("Pass")