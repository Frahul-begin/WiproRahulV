class Parent:
    def Parent1(self):
        print("Parent1")

class Child1(Parent):
    def c1(self):
        print("Child1")
class Child2(Parent):
    def c2(self):
        print("Child2")
#*
c1 = Child1()
c1.c1()
c2 = Child2()

c1= Child1()
c2.Parent1()
c2.c2()