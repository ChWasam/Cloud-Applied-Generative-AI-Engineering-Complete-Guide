# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greeting(name = "Wasam"):
    return print("Hi "+ name + " !")

greeting()
greeting("Ali")