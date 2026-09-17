num = int(input("Enter a number: "))

last_digit = num % 10
remaining = num // 10

if last_digit + remaining == num:
    print("It satisfies the condition.")
else:
    print("It does not satisfy the condition.")