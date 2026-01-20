import re

text = "pythonpowerful"
result = re.match("python", text)
if result:
    print("match found")
else:
    print("no match found")

searchresult = re.search("powerful", text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email = "admin@gmail.com"
if re.match(r"[a-zA-Z]+@", email):
    print("Valid email")
else:
    print("Invalid email")

result2=re.fullmatch(r"\d{10}", "123456789")
print(result2)

print(re.findall(r"\d+","price 50, 100 and 200"))

for n in re.finditer(r"\d+","A1, B33, c444"):
    print(n.group(), n.start(), n.end())

for n in re.finditer(r"[a-z]","A1, B33, c444"):
    print(n.group(), n.start(), n.end())

for n in re.finditer(r"[A-B]","A1, B33, c444"):
    print(n.group(), n.start(), n.end())

print(re.search(r"\d+", "Age is 24"))
print(re.search(r"^a.*c$", "abnskkkksjiiiu"))
m = re.search(r"\w+(?=@)", "test@gmail.com")
print(m.group())

print(re.search("python", "Python", re.I))

text4 = "one\ntwo\nthree"
print(re.findall(r"^t\w+", text4, re.M))


