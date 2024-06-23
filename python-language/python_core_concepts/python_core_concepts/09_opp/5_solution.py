# Problem5: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
#  yahan to function sa kia ha 
#  lakin polymorphism ham asa bhi karta han kah value kya da raha han 
#  for example plus ko no do to wo ausa add karwata ha aur agr string do to wo ausa mila data ha 



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


my_car = Car("honda","2022")
print(my_car.fuel_type())
# petrol or diseal

my_electric_car = ElectricCar("honda","2022", "125 KWH")
print(my_electric_car.fuel_type())
# Battery