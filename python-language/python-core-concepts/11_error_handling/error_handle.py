file = open('youtube.txt','w')  

# Jab bhi cautiously kam ho (databases ka sath interaction ho, ya files ka sath interaction ho ) we use try and catch

try:
    file.write('Chaudhry Wasam Ur Rehman')
finally:
    file.close()
# New and Better syntax
    
with open("youtube.txt",'w') as file:
    file.write('Chaudhry Wasam Ur Rehman')

# This method close file automatically
     


# __ (underscore)is known as dunder