# 1.
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print()
# 2.
s1 = student("Rahul",23)
s2 = student("Rohit",24)

# 3.
s1.display_details()
s2.display_details()