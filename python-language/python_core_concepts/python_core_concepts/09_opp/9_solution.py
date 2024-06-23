# Problem9: Demonstrate the use of isinstance() to check if my_electric_car is an instance of Car and ElectricCar.


class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
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



my_electric_car = ElectricCar("honda","2022", "125 KWH")
print(isinstance(my_electric_car,ElectricCar))
# True
print(isinstance(my_electric_car,Car))
# True 