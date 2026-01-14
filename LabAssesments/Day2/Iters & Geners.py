#Iterators & Generators

# 1.
print("Custom Iterator(1-N)")
class count:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current +=1
            return val
        else:
            raise StopIteration

obj = count(5)

for num in obj:
    print(num)
print("\n")

# 2.
print("Fibonacci series:")
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
for val in fibonacci(8):
    print(val)
print("\n")

# 3.

print("differ b/w Iter & Gener")
#Iterator
print("Iterator Output")
for x in count(5):
    print(x)

#Generator
def my_generator(n):
    for i in range (1 , n + 1):
        yield i
print("Generator Output:")
for x in my_generator(5):
    print(x)
