class MyError(Exception):
    pass
#raise MyError("This is a User defined exception")

class invalidage(Exception):
    pass

try:
    age = int(input("Enter an age"))
    if age < 18:
        raise invalidage("Age must be at least 18 or above")
    else:
        print("eligible to vote")
except invalidage as e:
    print("Error:", e)