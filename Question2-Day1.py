from enum import unique

data = [1, 2, 3, 4, 5, 6, 2, 4]

# 1.
sq_list = [x ** 2 for x in data]
print(sq_list)

# 2.
unique_even_numbers = {x for x in data if x % 2 == 0}
print(unique_even_numbers)

# 3.
cube_dict = {x : x ** 3 for x in data}
print(cube_dict)