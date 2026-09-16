salary=int(input("Enter salary: "))
years=float(float("Enter years of service: "))
if years >= 10:
    bonus = salary * 0.20
elif years >= 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.5
final_salary = salary + bonus
print("Bonus:", bonus)
print("final_salary:", final_salary )