# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance:int = int(input("Enter the distance that you are going to travel"))

if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")