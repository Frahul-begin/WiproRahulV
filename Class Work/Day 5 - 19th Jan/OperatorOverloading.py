class box1:
    def __init__(self, value):
        self.value = value

    def __add__(self, Nums):
        return self.value + Nums.value


b1 = box1(20)
b2 = box1(30)
b3 = box1(40)

result = b1 + b3
print(result)
