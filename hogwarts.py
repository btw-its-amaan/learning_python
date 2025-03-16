"""
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
    
    """

"""
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i+1, students[i]) "
    """
"""
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")

"""

students = [
    {"name": "Hermione", "house": "Griffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronous": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")