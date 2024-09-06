import pandas as pd
 
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'Gender': ['Male', 'Female', 'Male'],
    'Salary': [50000, 60000, 45000]
}


df = pd.DataFrame(data)
df.to_excel('C:\\Users\\DELL\\Downloads\\data.xlsx', index=False)  # index=False to omit row numbers
print("Data written to 'C:\\Users\\DELL\\Downloads\\data.xlsx'")


# Read the entire Excel file
df = pd.read_excel('C:\\Users\\DELL\\Downloads\\data.xlsx')
print("Data from Excel file:")
print(df)


# Reading only "Name" and "Salary" columns
df = pd.read_excel('C:\\Users\\DELL\\Downloads\\data.xlsx', usecols=["Name", "Salary"])
print(df)

# Reading only the first two rows
df = pd.read_excel('C:\\Users\\DELL\\Downloads\\data.xlsx', nrows=2)
print(df)


# Sorting by Age in ascending order
df_sorted = df.sort_values(by='Age', ascending=True)
print("Data sorted by Age:")
print(df_sorted)


# Renaming columns
df_renamed = df.rename(columns={'Name': 'Employee Name', 'Salary': 'Monthly Salary'})
print("Data with renamed columns:")
print(df_renamed)




