cars = [
            {"VIN":123,"Status":"OK"},
            {"VIN": 124, "Status": "OK"},
            {"VIN": 125, "Status": "Faulty"},
            {"VIN": 126, "Status": "OK"}
        ]
for car in cars:
    if car["Status"] == "Faulty" :
        print("Stopping Production line ...")
        break
    print(f"VIN:{car['VIN']} status is: {car['Status']} , shipping to customer" )
print("---------------------")
for car in cars:
    if car["Status"] == "Faulty" :
        print(f"VIN:{car['VIN']} status is: {car['Status']} , skipping to ship" )
        continue
    print(f"VIN:{car['VIN']} status is: {car['Status']} , shipping to customer" )
print("---------------------")
# else in for loop ; Used to print/execute a statement if the for loop executed successfully without encountering break
for car in cars:
    if car["Status"] == "Faulty" :
        print("Stopping Production line ...")
        break
    print(f"VIN:{car['VIN']} status is: {car['Status']} , shipping to customer" )
else:
    print("All cars successfully shipped without encountering break")   #  this will not be printed as the loop will encounter break
                                                                        # due to a faulty car in the list

for car in cars:
    if car["Status"] == "Faulty" :
        print(f"VIN:{car['VIN']} status is: {car['Status']} , skipping to ship" )
        continue
    print(f"VIN:{car['VIN']} status is: {car['Status']} , shipping to customer" )
else:
    print("All cars successfully shipped without encountering continue")    #  this will be printed as the loop will not encounter break
                                                                            # due to continue statement when it encounters faulty car
    # -Finding prime number with for loop
for n in range(2,20):
     for x in range(2,n):
         if n % x == 0:
             print(f"{n} equals {x} * {n//x}")
             break
     else:
         print(f"{n} is a prime number")
