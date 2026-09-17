a=float(input("Enate a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
disc = b ** 2 - 4 * a * c
if disc > 0:
    print("Two real and different roots.")
elif disc == 0:
    print("Two real and equal roots.")
else:
    print("No real roots.")