username = "Wasam"

def print_username():
    username = "ALI"
    print(username)

print_username()
print(username)


# closure and also known as factory functions 

#  bag theory


def a(num1):
    def b(num2):
        return num1 ** num2
    return b

ref_of_function = a(2)

print(ref_of_function(3))
#  is me to b ka ref gya ha isa ksa pta kah x me kya ha 
# yeh pecha wala sab variabkes  ka ref sath lata ha is akahta han bag theory



