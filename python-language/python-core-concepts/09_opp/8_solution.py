# Problem8: Use a property decorator in the Car class to make the model attribute read-only.
#  read only karna ha to private kar kah method ka through access karo
# We will use property decorator here (@property) 


class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def get_brand(self):

        return self.__brand + " !"

    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    
    def fuel_type(self):
        return("petrol or diseal")
    @property
    def model(self):
        return (self.__model) 
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size ):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return("Battery")


my_car = Car("honda","2022")
#  with @property you cannot access it like my_car.model()
#  you can access it as follows
print(my_car.model)






# petrol or diseal

# my_electric_car = ElectricCar("honda","2022", "125 KWH")
# print(my_electric_car.__model)
# Battery