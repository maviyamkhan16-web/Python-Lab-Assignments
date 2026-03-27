import pandas as pd

# Step 1: Create sample employee data
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["Automotive", "Finance", "Automotive", "IT", "HR"],
    "Designation": ["Developer", "Manager", "Developer", "Analyst", "Developer"]
}

df = pd.DataFrame(data)

# Save to Excel file
df.to_excel("employee.xlsx", index=False)
print("✅ employee.xlsx created successfully!\n")

# Step 2: Read the Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("\nEmployees in Automotive Domain:")
print(df[df["Department"] == "Automotive"])

# b) Details of employee by ID
emp_id = int(input("\nEnter Employee ID: "))
print(df[df["Employee_ID"] == emp_id])

# c) List of all Developers
print("\nList of Developers:")
print(df[df["Designation"] == "Developer"])