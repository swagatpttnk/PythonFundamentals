class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):          # <--- means subclass WorkingStudent inherits superclass Student
    def __init__(self, name, school, salary):
        # In python must call the super class constructor else will flag error. Try commenting both the __init()__ n see
        # Student.__init__(self,name, school)     # with Static method calls , u need to pass self
        super().__init__(name, school)  # with super() , its a method & u dont need to pass self
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 7

    @property  # @property can only be used with no parameter methods .(self is the default parameter)
    def monthly_salary(self):
        return self.salary * 30


rolf = WorkingStudent('Rolf', 'KVK', 12000)
print("rolf.salary={}".format(rolf.salary))
print("adding marks to rolf")
rolf.marks.append(88)
rolf.marks.append(96)
print("rolf.average={}".format(rolf.average()))

# @property decorators
print("rolf.weekly_salary()={}".format(rolf.weekly_salary()))
print("rolf.weekly_salary without decorators ={}".format(rolf.weekly_salary)) # without @property decorator will print the object address of the method 'weekly_salary'
# print(rolf.monthly_salary()) We shouldn't call () on a method declared with @property --> throws compilation error
print("rolf.monthly_salary with decorators={}".format(rolf.monthly_salary))  # with @property decorator will print the return value
