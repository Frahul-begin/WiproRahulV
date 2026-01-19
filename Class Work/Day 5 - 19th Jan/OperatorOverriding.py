class animal:
    def sound(self):
        print("animal is sounding")

class dog(animal):
    def sound(self):
        print("dog barking")

class cat(animal):
    def sound(self):
        print("cat meows")

obj = [dog(), cat()]

for a in obj:
    a.sound()
