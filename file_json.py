import os
import json

file_path = r"C:\Users\DELL\Downloads\data.json"

# 1. Writing to the JSON file
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Django", "REST API"]
}

with open(file_path, 'w') as file:
    json.dump(data, file )


# 2. Appending new data
with open(file_path, 'r') as file:
    data = json.load(file)

new_data = {
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles",
    "skills": ["JavaScript", "React"]
}

if isinstance(data, list):
    data.append(new_data)
else:
    data = [data, new_data]


with open(file_path, 'w') as file:
    json.dump(data, file)


# 3. Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

print("Current data in the file:", data)



# 4. Deleting the file
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("File deleted successfully")
# else:
#     print("The file does not exist")






