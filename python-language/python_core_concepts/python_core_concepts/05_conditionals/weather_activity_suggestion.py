# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather:str = input("How is weather today")
weather = weather.upper()

if weather == "SUNNY":
    print("Sggested Activily Based on weather: Go for a Walk")
elif weather == "RAINY":
    print("Sggested Activily Based on weather: Read a book")
elif weather == "SNOWY":
    print("Sggested Activily Based on weather: Build a snowman")

