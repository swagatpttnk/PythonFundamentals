cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']}{car['model']}"
    return name


def car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} goes {mpg} miles per gallon")  # since there is no return it is same as below line
    # return None


for car in cars:
    car_info(car)  # prints car info
    print(car_info(car))  # prints None because that is the return from a void function car_info

print("========= Divide function example =======")


def divide(x, y):  # this function outputs string if y==0 , else the result of the division
    if y == 0:
        return "You tried to divide by zero"
    else:
        return x / y


divide(10, 5)  # this returns 2 but won't be printed as we haven't handled the return value
print(f"printing the division result:{divide(10, 5)}")  # this returns 2 & will be printed

print("========= Default parameter Demo=======")


# def add(x=5,y): #compilation error [default value can only be at the end or all the variable should have default value
# def add(x=5,y=3): This is OK
def add(x, y=3):
    print(f"add function received x={x} , y={y}")
    total = x + y
    return total


print(f"total:{add(3, 5)}")  # prints 8
print(f"total:{add(3)}")  # prints 6         [formal argument 3 is called UnNamed Variable ]
print(f"total:{add(x=3, y=5)}")  # prints 8   [formal arguments x,y are called Named Variable ]
print(f"total:{add(y=4, x=5)}")  # prints 9   [arguments can be interchanged ]
print(f"total:{add(4, y=6)}")  # prints 10 [if 1st one is a unnamed variable , the next one may be a named one]

# print(f"total:{add(y=4,5)}") # compilation error [if 1st one is a named variable , the next must be a named one ]
# print(f"total:{add(y=4)}") # compilation error [ python will throw "missing 1 required positional argument"]

print("========= Function with variable as default parameter =======")
var_z = 3


def demo(x=5, y=var_z):  # This will work but highly discouraged . var_z =3 now.
    print(f"demo function received x={x} , y={y}")


demo(3)  # x=3 , y=3 default
var_z = 5
demo(3)  # x=3,y should default to 5, but y still default to 3 , thus using variable as default value is discouraged

print("========= Print function parameter =======")
print(1, 2, 3, 4, 5)  # prints 1 2 3 4 5
print(1, 2, 3, 4, 5, sep="-")  # prints 1-2-3-4-5
lst = ["aa", "bb", "cc", "dd"]
print(lst, sep="-")

print("========= Lamda functions =======")


def div(x, y):
    return x / y


print(f" div result:{div(4, 2)}")

div_lambda = lambda x, y: x / y

print(f" div_lambda result:{div_lambda(4, 2)}")

print(f" div_lambda2 result:{(lambda x, y: x / y)(4, 2)}")

print("========= Lambda functions Example 2  =======")

students = [
    {"name": "Rolf", "grades": (12, 34, 56, 23)},
    {"name": "Bob", "grades": (14, 34, 56, 23)},
    {"name": "Jen", "grades": (12, 22, 56, 64)},
    {"name": "Som", "grades": (12, 34, 43, 55)},
]

print("========= Without Lambda functions Example 2  =======")
def avg(sequence):
    return sum(sequence) / len(sequence)


for student in students:
    print(avg(student["grades"]))

print("========= With Lambda functions Example 2  =======")
avg_lamda = lambda seq: sum(seq) / len(seq)
for student in students:
    print(avg_lamda(student["grades"]))