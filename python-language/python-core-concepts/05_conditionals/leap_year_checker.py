# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
# print(4%4)
year:int = int(input("Enter Year"))

if (not year%400) or (not year%4 and year%100):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")