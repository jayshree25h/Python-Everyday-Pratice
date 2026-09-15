pur=float(input("Enter Purchasing Price: "))
sel=float(input("Enter Selling Price: "))
if sel > pur:
    print("Profit")
elif sel < pur: 
    print("loss")
else:
    print("Retail")
