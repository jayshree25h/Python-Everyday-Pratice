#An Armstrong number is a number where the sum of the cubes of its digits is equal to the original number
#Check Armstrong Number
num = int(input("Enter a number: "))

original = num
total = 0

while num > 0:
    
    digit = num % 10
    total = total + digit ** 3
    num = num // 10
    
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")