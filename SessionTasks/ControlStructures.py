from xml.sax.handler import property_dom_node

num = 7
if num%2 == 0:
    print("even")
else:
    print("Odd")
marks = 80

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")

for i in range(1,6):
    print(i)

    j=1
while j <= 5:
    print(j)
    j += 1

day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
