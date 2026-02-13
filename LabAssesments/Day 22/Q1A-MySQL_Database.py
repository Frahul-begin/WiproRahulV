import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "feb12"

conn = None

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    print("Connected successfully\n")

    # Fetch employees with Salary > 50000
    print("Employees with Salary > 50000:\n")

    fetch_query = "SELECT * FROM employe WHERE Salary > %s"
    cursor.execute(fetch_query, (50000,))

    for row in cursor.fetchall():
        print(row)

    # Insert new employee
    insert_query = """
    INSERT INTO employe (empid, empName, Salary)
    VALUES (%s, %s, %s)
    """

    new_employee = (106, "Kiran", 60000)
    cursor.execute(insert_query, new_employee)
    conn.commit()

    print("\nNew employee inserted successfully.")

    #Update salary by 10%
    employee_id = 101

    update_query = """
    UPDATE employe
    SET Salary = Salary * 1.10
    WHERE empid = %s
    """

    cursor.execute(update_query, (employee_id,))
    conn.commit()

    print("Salary updated successfully (10% increment).")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if conn is not None and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
