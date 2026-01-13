add = lambda x, y: x + y
print(add(5, 8))

multi = lambda x, y: x * y
print(multi(12, 6))

maxnum = lambda x, y: x if x > y else y
print(maxnum(21,20))

#map(function, iteratable)
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))

result = map(lambda x: x ** 2, numbers)
print(list(result))