# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# items:list = ["apple", "banana", "orange", "apple", "mango"]

# duplicate:bool = False

# for item in items:
#     if items.count(item) > 1:
#         print(item)
#         duplicate = True
#         break

# if duplicate == False:
#     print("Duplicate not found")


# Answer provided by Sir
items:list = ["apple", "banana", "orange", "mango", "orange"]
unique_items:set = set()

for item in items:
    if item in unique_items:
        print("Duplicate Item Found:", item)
        break
    unique_items.add(item)


    



        