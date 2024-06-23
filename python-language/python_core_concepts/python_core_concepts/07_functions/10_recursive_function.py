# Problem: Create a recursive function to calculate the factorial of a number.

# Recursive ak technique h a programming ke jis me ap function kowapis sa call karta rehta ho function ka andar sa hi 
# Is me main kam yeh ha kah exit strategy socho 


def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 
    
print(factorial(4))
