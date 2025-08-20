friends = ["Rolf", "Randy", "Kevin", "Gons"]
print(f'friend list original:{list(friends)} ')

# ---------------------- Any & All ---------------
mylist = ["Rolf", "Randy", "Kevin", ""]
print(f'mylist any:{any(mylist)} all:{all(mylist)} ')
# "" <-- false


mylist = [1, 6, "0.0", 0.0]
print(f'mylist any:{any(mylist)}'
      f' all:{all(mylist)} ')
# 0.0 <-- false