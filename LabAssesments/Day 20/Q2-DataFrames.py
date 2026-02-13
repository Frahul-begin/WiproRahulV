import pandas as pd

# Step 1: Create DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filter employees from IT department
it_employees = df[df["Department"] == "IT"]

print("\nEmployees from IT Department:")
print(it_employees)

# Find average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary per Department:")
print(avg_salary)

# Add Salary_Adjusted column (+10%)
df["Salary_Adjusted"] = df["Salary"] * 1.10

print("\nDataFrame after Salary Adjustment:")
print(df)
