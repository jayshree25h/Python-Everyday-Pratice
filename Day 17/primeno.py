# Check wheather a number is prime using while

num = int(input("Enter a number: "))

i = 2
is_prime = True

if num < 2:
    is_prime = False

while i < num:
    if num % i == 0:
        is_prime = False     
        break
    i = i + 1
if is_prime:
    print("Prime number")
else:
    print("Not a Prime number")