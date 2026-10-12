# Find Prime Numbers Using Nested Loops

for num in range(2, 51):
    
    is_prime = True
    
    for divisor in range(2, num):
        
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)