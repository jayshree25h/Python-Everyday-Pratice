price = float(input("Enter product price: "))

if price >= 5000:
    discount = price * 0.20
elif price >= 2000:
    discount = price * 0.10
else:
    discount = 0 
final_price = price - discount

print("Discount:", discount)
print("Final Price: ", final_price)