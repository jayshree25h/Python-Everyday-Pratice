password = input("Enter your password: ")

if len(password) >= 8 and password != "password":
    print("Password is acceptable.")
else:
    print("Password is weak.")
