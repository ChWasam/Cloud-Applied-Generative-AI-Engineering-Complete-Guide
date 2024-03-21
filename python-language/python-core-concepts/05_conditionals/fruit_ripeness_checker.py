# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit:str = "Banana" 
color:str = input("Enter color of fruit")

if color == "Green":
    print(fruit,"is Unripe")
elif color == "Yellow":
    print(fruit,"is Ripe")
elif color == "Brown":
    print(fruit,"is Overripe")