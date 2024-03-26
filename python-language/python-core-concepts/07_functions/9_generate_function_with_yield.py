# problem: Write a generator function that yields even numbers up to a specified limit.
   

# def even_numbers (num):
    
#     for i in range(2,num+1,2):
#         print(i)

# even_numbers(10)

#  lakin is code me me isa use to nahi kar sakta ho  ku kah return to kia nahi ha
#  return karain ga to masla ai ga 

# list me ak ak value dal kah return kar sakta ho magar mujha to ak ak value return me chahia  

#  value ko yield karna ka matlab ha value ko generate karna aur function ko memory me yad bhi rakho  ta kah next time jab me ap ko call karo to ap mujha wahan sa value wapis do aur jo bhi agae alag alag loop call kar raha ha asua alag alag memory me reference rakho

#  value yield bhi return karta ha magar memory me aus function ko rakhta ha  
#  Aur aus ke state ko bhi rakhta ha kah abhi ap itna kam kar chuka ho 

def even_numbers_generator (num):
    for i in range(2,num+1,2):
        yield  i 
I = iter(even_numbers_generator(10))

for num in even_numbers_generator(10):
    print(num)


#  checked the internal working on python shell 

# Last login: Sat Mar 23 14:52:47 on ttys102
# wasamchaudhry@Chaudhrys-MacBook-Pro ~ % python3 
# Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> def even_numbers_generator (num):
# ...     for i in range(2,num+1,2):
# ...         yield  i 
# ... 
# >>> I = iter(even_numbers_generator(10))
# >>> next(I)
# 2
# >>> 
# >>> next(I)
# 4
# >>> next(I)
# 6
# >>> next(I)
# 8
# >>> next(I)
# 10
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration