avg = lambda seq:sum(seq)/len(seq)
total = lambda seq:sum(seq)
top = lambda seq:max(seq)

students = [
    {"name": "Rolf", "grades": (12, 34, 56, 23)},
    {"name": "Bob", "grades": (14, 34, 56, 23)},
    {"name": "Jen", "grades": (12, 22, 56, 64)},
    {"name": "Som", "grades": (12, 34, 43, 55)},
]
print("========= Without FirstClass functions Example 3  =======")
for student in students:
    name = student["name"]
    grade = student["grades"]

    print(f"Student:{name}")
    operation = input ("Enter 'average','total' or 'top' :")
    if operation.lower() == "average":
        print(avg(grade))
    elif operation.lower() == "top":
        print(top(grade))
    elif operation.lower() == "total":
        print(total(grade))


print("========= With FirstClass functions Example 3  =======")
operations = {
    "average": avg,
    "total": total,
    "top": top
}
for student in students:
    name = student["name"]
    grade = student["grades"]

    print(f"Student:{name}")
    operation = input ("Enter 'average','total' or 'top' :")
    print(operations[operation](grade))
