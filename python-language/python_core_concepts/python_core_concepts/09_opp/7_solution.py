# Problem7: Add a static method to the Car class that returns a general description of a car.
# Static method :  Asa method jo class ka pass to available ha lakin instance(object) ka pass nahi ha. matlab ham class sa access kar sakain lakin object sa na kar sakain
#  we will use @staticmethod right before the function defintion
# and this @staticmethod is called decorator


#  But while practicing i discovered that using static method make it accessible by both instance and class


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
    @staticmethod
    def car_description():
        return("Cars are means of transport")
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size ):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return("Battery")


my_car = Car("honda","2022")
print(my_car.car_description())
#  Ham chahta han kah my_car access na kar pai 

print(Car.car_description())




