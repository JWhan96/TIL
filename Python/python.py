import math
numbers = [1, 4, 9, 16, 25]

sqrt_numbers = []
for number in numbers:
    if number % 2 ==0:
        sqrt_numbers.append(int(math.sqrt(number)))
#list comprehension
sqrt_numbers2 = [int(math.sqrt(number)) for number in numbers if number%2==0 ]

print(sqrt_numbers)
print(sqrt_numbers2)