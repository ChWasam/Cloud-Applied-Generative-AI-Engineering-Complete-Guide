# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# polymorphism (python isa by default kar data ha)
#  matlab ak operator (e.g *) string aur number dono ko handle kar lata ha 

print(5 * 5)
# 25
print("l" * 5) 
# lllll

#  Solution 

def multiply (p1 ,p2):
    return (p1 * p2)

print(multiply(3,3))
print(multiply(3,"h"))
print(multiply("h",3))


