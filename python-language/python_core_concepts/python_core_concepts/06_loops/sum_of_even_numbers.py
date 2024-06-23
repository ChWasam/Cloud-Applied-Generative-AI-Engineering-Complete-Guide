# Problem: Calculate the sum of even numbers up to a given number n.

number : int = int(input("Enter a number up to which you want to calclate sum of even numbers"))
sum_of_even_numbers:int = 0

for i in range(1,number+1):
    if i%2 == 0:
        sum_of_even_numbers = sum_of_even_numbers+ i

print(sum_of_even_numbers)



