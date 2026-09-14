#check largest of three number (pridefined is a program user input )

a = int(input("Enter the First No:"))
b = int(input("Enter the second No:"))
c = int(input("Enter the third No:"))

if a >= b and  a >=c : # both the condition is true then return true 
    print("A is largest")
elif b >= a and  b >= c :
    print ("B is largest")
else:
    print ("C is Largest")
