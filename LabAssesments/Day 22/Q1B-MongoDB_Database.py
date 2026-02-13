from pymongo import MongoClient

try:
    # 1️⃣ Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB successfully\n")

    # Access database and collection
    db = client["company_db"]
    collection = db["employees"]

    # 2️⃣ Insert a new employee document
    new_employee = {
        "name": "Rahul",
        "department": "IT",
        "salary": 65000
    }

    collection.insert_one(new_employee)
    print("New employee document inserted.\n")

    # 3️⃣ Find all employees in IT department
    print("Employees in IT department:\n")

    for emp in collection.find({"department": "IT"}):
        print(emp)

    # 4️⃣ Update salary of employee with given name
    collection.update_one(
        {"name": "Rahul"},            # condition
        {"$set": {"salary": 70000}}   # new salary
    )

    print("\nSalary updated successfully.")

except Exception as e:
    print("Error:", e)

finally:
    client.close()
    print("\nMongoDB connection closed.")
