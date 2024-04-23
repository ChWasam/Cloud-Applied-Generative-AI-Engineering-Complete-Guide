# Problem1: Create a Car class with attributes like brand and model. Then create an instance of this class.
# OOP me ak form hi to bnana ka  matlab ak model create karna ha 
#  attriutes ka matlab ha kah khuch variables bnana han 
# instance matlab ak form lo aur ausa ak user ko bharna ha bas 
#  jasa def ak keyword ha wasa class bhi ak keyword ha 
#  name of class is always capital 

# my_car aur Car ko link karna ka lia 
# def _init_(self, userbrand, usermodel) :        Is me jo self use kia ha is ka through connection banta ha 
# self ka matlab ha jis na bhi call kis 
#  aupar jo __init__ ha isa constructor bhi kaha jata ha 
#  Constructor wo method ha kah jasa hi object banta ha kisi bhi class sa to sab sa pehla yeh method call ho jata ha 

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model


# Aksar is class ko seperate file me bna kah rakh dia jata ha  jab bhi use karna ha isa import karwa lo  aur variables bnata jao aur use karo
 
my_first_car = Car("toyota","2024")
print(my_first_car.brand)
print(my_first_car.model)

my_second_car = Car("honda","2022")
print(my_second_car.brand)
print(my_second_car.model)

# my_car me ab ak object ha is class ka 
# matlab ak copy nikal kah ai ha 

