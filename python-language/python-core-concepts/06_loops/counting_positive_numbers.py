# Problem: Given a list of numbers, count how many are positive.

numbers:list = [1, -2, 3, -4, 5, 6, -7, -8, 9,45,15, 10]
count_of_positive_number:int = 0
for number in numbers:
    if number > 0:
        count_of_positive_number+= 1
print("Total count of positive numbers is:", count_of_positive_number)
        

