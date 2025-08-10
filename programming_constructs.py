friend = "Annie"
user_name = input("Input username :")
if user_name == friend:
        print(f"Hello Friend, {user_name}")
        print("This runs too")

    # print("This runs again")   <--- this will throw error as the indentation is not with hte 1st 4 lines
else:
    print("Else part executed")
print("This runs at the end ")
print("----- milestone 1 -----")



name = input ("Input a string:")
if name:
     print(f"inputed name:{name}")
print("----- milestone 3 -----")

# #### -----While , do-while , for loop
# -----While
user_input = input("Do u wish to run the sigma program [yes/no]: ?")
while user_input == "yes":
    print("we are running...")
    user_input = input("Do u wish to continue with sigma [yes/no]: ?")

print("we exited sigma running...")
# -----do While
# ----- For-Each
friends = ["Annie","Sppt","Gary"]
for friend in friends:
    print(f"Hello {friend}")

elements = [1,2,3,4,5]
for _ in elements:      # underscore represents that the variable is not going to be used in the for body
    print("Hello World")

for index in range(5): # range(start , stop , step ),ex: range(2,20,3) --> 2,5,8,11,14,17
    print(f"Hello World {index}")

students = [
    {"name":"Rolf","grade":90},
    {"name":"Ann","grade":34},
    {"name":"Rek","grade":69}
]
for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")

