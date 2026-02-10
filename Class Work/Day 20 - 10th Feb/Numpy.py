import numpy
import pandas as pd
arr=numpy.array([1,2,3,4,5])

print("array:", arr)
print("sum", numpy.sum(arr))
print("mean", numpy.mean(arr))
print("min", numpy.min(arr))
print("max", numpy.max(arr))
print("multiply by 2", arr*2)

data= {
    "Name":["Rahul","Rohit","ravi"],
    "Age":[24,25,27],
    "City":["Bangalore","Chennai","Hyderabad"]

}

df=pd.DataFrame(data)
print(df)

print(df["Name"])

print(df[df["Age"]>26])
df["Salary"]=[50000,600000,700000]
print(df)

