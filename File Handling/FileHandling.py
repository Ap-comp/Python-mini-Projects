import csv
import json

# ---------- TEXT FILE HANDLING ----------

# Write to a text file
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nSecond line.")

# Read from a text file
with open("sample.txt", "r") as file:
    text = file.read()
    print("Text file content:")
    print(text)

# ---------- CSV FILE HANDLING ----------

# Create a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Ravi", 24])
    writer.writerow(["Priya", 32])
    writer.writerow(["Amit", 29])

# Read CSV file using DictReader and filter age > 25
print("\nPeople aged above 25 from CSV:")
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["age"]) > 25:
            print(row["name"], "-", row["age"])

# ---------- JSON FILE HANDLING ----------

# Create and write JSON data
student_data = {
    "students": [
        {"name": "Ravi", "age": 24},
        {"name": "Priya", "age": 32}
    ]
}

with open("students.json", "w") as file:
    json.dump(student_data, file, indent=4)

# Read JSON file and print names
print("\nStudent names from JSON:")
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data["students"]:
        print(student["name"], "-", student["age"])