# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


age:int = int(input("Enter Age"))
day: str = input("Enter Day Today")

price:int = 12 if age >=18 else 8

if day == "wednesday":
    print("price: $", price-2)
else:
    print("price: $", price)



