# Check Whether a Number is Palindrome
#A palindrome is a number that reads the same forward and backward, such as 121, 1331, or 555.
num = int(input("Enter a number: "))

original = num 
reverse  = 0

while num > 0:
    
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")