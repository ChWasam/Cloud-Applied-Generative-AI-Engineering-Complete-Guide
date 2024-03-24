# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number:int = int(input("Enter the number"))
    if 1<= number <=10:
        print("Number is between 1 and 10")
        break
    else:
        print("Enter number again between 1 and 10")
