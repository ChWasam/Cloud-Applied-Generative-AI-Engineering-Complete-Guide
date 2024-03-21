# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet:str = input("Enter pet Species")
pet_age:int = int(input("Enter pet age"))

if pet =="dog":
    if pet_age < 2:
        print("puppy food")
    else:
        print("Dog Food")
elif pet =="cat":
    if pet_age <= 5:
        print("Junior Cat Food")
    else:
        print("Senior Cat Food")
    
