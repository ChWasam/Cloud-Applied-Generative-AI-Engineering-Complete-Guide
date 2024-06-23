# Problem: Compute the factorial of a number using a while loop.

# Factorila of 5 is 5*4*3*2*1 

number:int = int(input("Enter a number"))

actual_number:int = number
factorial:int = 1

while number > 0:
    factorial = number * factorial
    number = number - 1

print("Factorial value of number ", actual_number, "is :",factorial) 

