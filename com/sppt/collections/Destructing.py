"""
 Destructuring means assigning elements back to variables
 Benefit : 1.Writing cleaner, more readable code
           2.Extracting multiple values in loops and function arguments
           3.Supporting more flexible and dynamic patterns in modern Python (e.g. with match)
"""



# destructuring  a tuple/list in for loop ----
students = [
    ("Rolf",90),
    ("Ann",34),
    ("Rek",69)
]
student1,student2,student3 = students
print(f"Student Name:{student1[0]} Grade:{student1[1]}")
print(f"Student Name:{student2[0]} Grade:{student2[1]}")
print(f"Student Name:{student3[0]} Grade:{student3[1]}")

for student in students:
    name = student[0]
    grade = student[1]
    print(f"Prodigy {name} has a grade of {grade}")
for student in students:
    name,grade = student
    print(f"Scholar {name} has a grade of {grade}")
for name,grade in students:
    print(f"Student {name} has a grade of {grade}")

studentsDictionary = [
    {"name":"Greg","grade":93},
    {"name":"Sam","grade":29},
    {"name":"Noel","grade":99}
]
student1,student2,student3 = studentsDictionary
print(f"Student Name:{student1['name']} Grade:{student1['grade']}")
print(f"Student Name:{student2['name']} Grade:{student2['grade']}")
print(f"Student Name:{student3['name']} Grade:{student3['grade']}")

# destructuring a dictionary in for loop ----
# style 1
for student in studentsDictionary:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")
# style 2
for student in studentsDictionary:
    key1,key2 = student.keys()
    print(f"{student[key1]} has grade {student[key2]}")
# style 3
for student in studentsDictionary:
    studentname=''
    grade =0

    for key,value in student.items():
        if key == "name":
            studentname = value
        elif key == 'grade':
            grade =value

    print(f"This student {studentname} has grade {grade}")


#Pattern Matching (Python 3.10+)
person = {"name": "Sam", "age": 28}

match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
