# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_coffee_size:str = input("Enter coffee size you want to order")

extra_shot:bool = bool(int(input("For extrashot press 1 and press 0 if you don't want")))

if extra_shot:
    print("Order:", order_coffee_size ,"cup of coffee with Extra Shot of espresso")
else:
    print("Order:", order_coffee_size,"cup of coffee" )