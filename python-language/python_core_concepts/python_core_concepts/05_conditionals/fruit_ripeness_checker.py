# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit:str = "Banana" 
color:str = input("Enter color of fruit")
color = color.upper()
# print(color)

if color == "GREEN":
    print(fruit,"is Unripe")
elif color == "YELLOW":
    print(fruit,"is Ripe")
elif color == "BROWN":
    print(fruit,"is Overripe")