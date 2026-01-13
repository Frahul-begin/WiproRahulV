try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Can't divide by zero")

try:
    x = int(input("Enter a number"))
    print(10/x)
except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Execution is Successful")
