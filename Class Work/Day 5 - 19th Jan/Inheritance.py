class Animal:
    def speak(self):
        print("Animal is speaking")

class dog(Animal):
    def bark(self):
        print("Dog Barks")

d = dog()
d.speak()
d.bark()