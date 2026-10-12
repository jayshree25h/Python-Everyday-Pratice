number = 1

for i in range(1, 6):
    
    for j in range(i):
        
        if number == 16:
            break
        
        if number % 5 == 0:
            number = number + 1
            continue
        
        print(number, end= " ")
        number = number + 1
        
    print()
    
    if number == 16:
        break