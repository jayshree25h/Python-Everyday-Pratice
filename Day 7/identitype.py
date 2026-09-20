vegetables = ["tomato", "potato", "chilli"]

vegetable = input("Enter a vegetable name: ")

if vegetable in vegetables:
    print("Vegetable is available.")
else:
    print("Vegetable is not available.")

if "coriander" not in vegetables:
    print("Coriander is not available.") 