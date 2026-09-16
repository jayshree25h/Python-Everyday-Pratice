amount = float(input("Enter shopping amount: "))
member = input("Are you a member? (yes/no): ")

if amount >= 2000 and member == "yes":
    print("You get a 20% discount.")

elif amount >= 2000 or member == "yes":
    print("You get a 10% discount.")

else:
    print("No discount.")
