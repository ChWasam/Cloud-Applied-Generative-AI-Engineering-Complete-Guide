# Given a string, find the first non-repeated character.

my_string :str = "teetereervooepirnjn"


for char in my_string:
    if my_string.count(char) == 1:  
        # Matlab agar yeh wala character is pori string me 1 dafa aya ha 
        #  Loop individual character pa lag raha ha 
        print("Character is :", char)
        break

