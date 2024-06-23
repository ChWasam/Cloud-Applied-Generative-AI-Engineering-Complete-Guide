#  Problem3: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.(Inheritance)
     

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return (f"{self.brand} {self.model}")
    
class ElectricCar(Car):
# bas car add karna tha aus ke sab cheezain mil jati han 
    def __init__(self,brand,model,battery_size ):
#  batan aka lia kah yeh kam super me ho chuka ha 
#  super matlab apna sa aupar
        super().__init__(brand,model)
        self.battery_size = battery_size



my_car = ElectricCar("honda","2022", "125 KWH")
print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car.full_name())
