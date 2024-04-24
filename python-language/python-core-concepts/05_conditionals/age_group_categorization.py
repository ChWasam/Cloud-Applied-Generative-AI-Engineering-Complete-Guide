# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


age :str = input("Enter the age of a person")
print(type(age)) 
# <class 'str'>
int_age:int = int(age)
print(type(int_age))
# <class 'int'>

if int_age < 1:
    print("Enter Correct age")
    exit()
else:
    if int_age < 13:
        print("Child")
    elif int_age < 19:
        print("Teenager")
    elif int_age < 59:
        print("Adult")
    else:
        print("Senior")

