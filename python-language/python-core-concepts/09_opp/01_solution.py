# Problem1: Create a Car class with attributes like brand and model. Then create an instance of this class.
# Problem2: Add a method to the Car class that displays the full name of the car (brand and model).
# Problem5: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
# Problem6: Add a class variable to Car that keeps track of the number of cars created.

# Problem7: Add a static method to the Car class that returns a general description of a car.
# Static method :  Asa method jo class ka pass to available ha lakin instance ka pass nahi ha. matlab ham class sa access kar sakain lakin object sa na kar sakain
#  we will use @staticmethod right before the function defintion
# and this @static method is called decorators

# Problem8: Use a property decorator in the Car class to make the model attribute read-only.
#  read only karna ha to private kar kah method ka through access karo
# We will use property decorator here (@property) 

# Problem9: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
# Problem10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

# Class name should always start with capital letter 

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        # self.total_car +=1

    def get_brand(self):
        return self.__brand + " ! "
    
    def full_name(self):
        return f"{self.__brand}  {self.__model}"
    
    def fuel_type(self):
        return "Petrol"
    
    @staticmethod
    def general_description():
        return "Car is a great invent"
    
    @property
    def model(self):
        return self.__model
    

#  Problem3: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.(Inheritance)
     
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Battery"
    



my_tesla = ElectricCar("Tesla","Mark S" ,"200KWh")
print(isinstance(my_tesla,ElectricCar))
print(isinstance(my_tesla,Car))
print(my_tesla.battery_size)
# print(my_tesla.__brand)
# AttributeError: 'ElectricCar' object has no attribute '__brand'.
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.fuel_type())

# Problem4: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.(Encapsulation )
# matlab yeh kah capsule ka andar jo bhi ha wo mera chahna pa hi ap ko pta laga 


my_car = Car("Totota" , "Corolla")
 
# my_car is an object
#  Car() is a class

print(my_car.model)

print(Car.total_car)

# print(my_car.__brand)
# # AttributeError: 'Car' object has no attribute '__brand'
print(my_car.get_brand())

print(my_car.full_name())
print(f"Fuel Type : {my_car.fuel_type()}")
# static method
print(Car.general_description())

# Property decorator

print(my_car.model)

# my_new_car = Car("Hundai" ,"Elantra")
# print(my_new_car.model)
# print(my_new_car.full_name())

# Problem10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is Battery"
class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_electric_car = ElectricCarTwo("Hyndai","Tuson")

print(my_new_electric_car.model)
print(my_new_electric_car.engine_info())
print(my_new_electric_car.battery_info( ))

