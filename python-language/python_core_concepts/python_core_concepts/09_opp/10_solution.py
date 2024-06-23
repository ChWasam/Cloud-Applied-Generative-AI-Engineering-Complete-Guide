# Problem10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def __init__(self,battery_life,battery_type):
        self.battery_life = battery_life
        self.battery_type = battery_type

class Engine:
    def __init__(self,engine_CC,condition):
        self.engine_CC = engine_CC
        self.condition = condition

class ElectricCar(Battery,Engine):
    def __init__(self,brand,battery_life,battery_type,engine_CC,condition):
        # super().__init__(battery_life,battery_type,CC,condition)
        # When using super().__init__(), you need to pass arguments only for the immediate parent class
        # Since ElectricCar inherits from both Battery and Engine, you should call their constructors separately in your ElectricCar class. Here's how you can fix it:

        Battery.__init__(self, battery_life, battery_type)  
        Engine.__init__(self, engine_CC, condition)  

        self.brand = brand

my_electric_car = ElectricCar("Tesla","5 years","Neon","5000CC", "10/10")

print(my_electric_car.battery_life)
print(my_electric_car.condition)
print(my_electric_car.battery_type)
print(my_electric_car.brand)
print(my_electric_car.engine_CC)


