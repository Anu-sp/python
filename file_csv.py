import os
import csv

file_path = r"C:\Users\DELL\Downloads\data.csv"

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open (file_path, mode ='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to the CSV file successfully.")
print(data)

# Data to append
new_data = [
    ['David', 28, 'San Francisco'],
    ['Eve', 22, 'Boston']
]

with open (file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print("Data appended to the CSV file successfully.")
print(data)

# Read the CSV file
with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Delete the CSV file
# if os.path.exists(file_path):
#     os.remove(file_path)
# else:
#     print("The file does not exist")