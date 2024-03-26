# Problem: Write a function that takes variable number of arguments and returns their sum.
#  *args (* zaroori ha is ka sath khuch bhi likh sakta ha )
# Lakin achi practice yeh ha kah isa *args hi likhain  


def add (*args):
    print(*args)
    print(args) 
    # args will give result in tuples
    
    sum_of_all_values_in_args = 0
    for i in args:
        sum_of_all_values_in_args += i
    print(sum_of_all_values_in_args)
    
    return sum(args)

print(add(2,4,8))
  