balance=float(input("Enter balance amount: "))
amount=float(input("Enter Withdrawal amount: "))
if amount <= balance and amount > 0:
    balance = balance - amount
    print("withrawal successful. ")
    print("Remaining balance:" , balance)
else:
    print("Invalid withdrawal.")