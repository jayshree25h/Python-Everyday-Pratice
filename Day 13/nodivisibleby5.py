count = 0  # Use for when you generally know how manytimes you want to repeat something.
for i in range ( 1, 101):
    if i % 5 ==0:
        count = count + 1
print("count:" , count)