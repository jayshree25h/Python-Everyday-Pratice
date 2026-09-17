balance = 10000
correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
            print("New balance:", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:", balance)

        else:
            print("Invalid withdrawal amount.")

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN.")
    