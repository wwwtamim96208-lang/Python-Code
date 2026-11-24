#Dictionaries
student = {
    "name": "Rahim",
    "age": 21,
    "department": "CSE",
    "cgpa": 3.75
}

print(student)
print(student["name"])
print(student["cgpa"])

student["age"] = 22
student["semester"] = 8

print(student)

#Loop through dictionary
student = {
    "name": "Rahim",
    "age": 21,
    "department": "CSE"
}

for key, value in student.items():
    print(key, ":", value)