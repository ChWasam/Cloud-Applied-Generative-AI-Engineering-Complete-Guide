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
for num in even_numbers_generator(10):
    print(num)