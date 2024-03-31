# Problem2: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = (", ").join( str(arg) for arg in args)
        kwargs_value = (", ".join(f"{key}:{value}" for key,value in kwargs.items()))
        
        result = func(*args,**kwargs)
        print(f"Name of Function :{func.__name__} with args :{args_value} and kwargs :{kwargs_value}")
        return result
    
    return wrapper



@debug
def office_profile(name, father_name ,designation = "Softwar Engineer"):
    print(f"name : {name} , Father Name :{father_name} , Designation : {designation}")

office_profile("Chaudhry Wasam Ur Rehman", "Chaudhry Safdar ALI" ,designation = "Softwar Engineer")

@debug
def add(num1,num2):
    print(num1 + num2 )

add(4,2)


#  Simplest decorator matlab yeh to har decorator me ho ga hi 

# def debug(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper