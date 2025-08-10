class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Swagat",[66,72,85,92])
student2 = Student("Caldy",[34,55,85,65])
print(f"Student 1 average:{student1.average()}")
print(f"Student 2 average:{student2.average()}")
print(f"Student 1 average:{Student.average(student1)}")
print(f"Student 2 average:{Student.average(student2)}")
print(f"Class of student2:{student2.__class__}")
movie = ["Loads of Rings","Interstellar","Topgun"]
print(f"Class of movie[] :{movie.__class__}")
print(f"Class of \"AASD\" :{"AASD".__class__}")