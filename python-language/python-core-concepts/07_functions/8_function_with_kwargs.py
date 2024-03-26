# Problem: Create a function that accepts any numbe r of keyword arguments and prints them in the format key: value.

def print_kwargs (**kwargs):
    print(kwargs)
    #  kwargs gives object
    for key,value in kwargs.items():
        print(f"{key} : {value}") 
    
   

print_kwargs(name = "wasam" , designation = "Generative AI Engg")