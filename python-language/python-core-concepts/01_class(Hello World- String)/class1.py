print("wasam")

# name : str = 700  # Getting error which means mypy extention is active 

# print(name)S


# to see error in line 3 you can also type " mypy class1.py " in terminal\
# In terminal 
#mypy class1.py 
# Result 
# error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 1 error in 1 file (checked 1 source file)



name : str = "Chaudhry Wasam Ur Rehman"
print (name)
print(type(name))
print(id(name))