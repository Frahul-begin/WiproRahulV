student={
    "name": "Rahul",
    "age": 25,
    "Course": "Python"
}

print(student)
print(student["name"])
print(student.get("age"))
student["Marks"]=95
student["Age"] = 30
print(student)

print(student["name"])
print(student.get("age"))
student.pop("age")
print(student)

student.popitem()
print(student)
print(student.keys())
print(student.values())

for key in student:
    print(key,student[key])

if "name" in student:
    print("key exists")

employee={
    101:{"name":"rahul", "salary": 10000},
    102:{"name":"Rohit", "salary": 8000}
}