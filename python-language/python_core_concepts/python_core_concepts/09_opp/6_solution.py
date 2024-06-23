# Problem6: Add a class variable to Car that keeps track of the number of cars created.



class Car:
    total_car =0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
#  we can use self.total_car or Car.total_car
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return (f"{self.__brand} {self.model}")
    
    def fuel_type(self):
        return("petrol or diseal")
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size ):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return("Battery")


my_car = Car("honda","2022")
# print(my_car.fuel_type())

Car("Toyota","2018")
my_electric_car = ElectricCar("honda","2022", "125 KWH")
# print(my_electric_car.fuel_type())

#  We can access total car directly as it is a class variable
print(Car.total_car)
