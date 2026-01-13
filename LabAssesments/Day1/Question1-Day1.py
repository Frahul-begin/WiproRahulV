from functools import reduce

#1
numbers = list(range(1, 21))
print(numbers)

#2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#3
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))
print(squared_even_numbers)

#4
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)
print(sum_of_squares)

#5
for index, value in enumerate(squared_even_numbers):
    print(f" {index}: {value}")

print("Sum of squared even numbers:", sum_of_squares)