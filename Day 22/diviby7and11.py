# Find the First Number Divisible by Both 7 and 11
for i in range(1, 501):
    
    if i % 7 == 0 and i % 11 == 0:
        print("First number:", i)
        break