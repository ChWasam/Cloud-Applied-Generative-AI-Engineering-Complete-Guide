# Problem: Check if a number is prime.

#  Prime number is a whole number > 1    divisible by itself only 

number:int = int(input("Enter a number"))
flag:bool = True
if number >1:
    for i in range(2,number):
        if i!=number  and number%i == 0:
            print("Number is not prime")
            flag = False
            break

if flag == True:
    print("Number is prime")



# number = 28

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)


        

