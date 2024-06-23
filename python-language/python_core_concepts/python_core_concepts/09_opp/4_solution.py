# Problem4: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.(Encapsulation )
# matlab yeh kah capsule ka andar jo bhi ha wo mera chahna pa hi ap ko pta laga
#  mera chahna pa hi pta chala kah is ka andar kya ha 
#  matlab brand ka andar kya ha yeh access me nahi rah ga 
#  provide a getter method for it ta kah log ausa access kar pai lakin method sa access karain ga  



class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

#  private karna ka lia pehla to __brand karna para ga 
# matlab yeh ha kah wo class ka andar to access ho sakta ha magar object ab ausa access nahi kar pai ga 
    
    def get_brand(self):
# get_brand syantax for getter function
        return self.__brand + " !"

    def full_name(self):
        return (f"{self.__brand} {self.model}")
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size ):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = Car("honda","2022")
# print(my_car.__brand)
print(my_car.get_brand())

# my_car = ElectricCar("honda","2022", "125 KWH")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.battery_size)
# print(my_car.full_name())