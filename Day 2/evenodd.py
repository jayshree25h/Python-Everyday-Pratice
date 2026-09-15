num=int(input("Enter a number: "))
if num >= 0:
    if num % 2 == 0:
        print("Positive Even no.")
    else:
        print("Positive Odd no. ")
else:
    if num % 2 == 0:
        print("Negative Even no. ")
    else:
        print("Negative Odd no.")
