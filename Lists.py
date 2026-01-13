numbers=[10,20,30,40]
names=["Ram","Hari","Ramhya"]
mixed=[1,"Pthon",3.5,True]

numbers[1]=100
print(numbers)
print(names)
print(mixed)


for i in numbers:
    print(i)

if 10 in numbers:
    print("Found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

names.reverse()
print(names)

names.append("ranjit")
print(names)

names.extend(("rohan", "rohit"))
print(names)

names.remove("ranjit")
print(names)

names.insert(4, "roshan")
print(names)