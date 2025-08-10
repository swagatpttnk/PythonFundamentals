class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):              # if u define this method in a class , it enables the call of len(obj) on it.
        return len(self.cars)

    def __getitem__(self, item):    # if u define this method in a class , it enables the call of obj[index] on it.
        return self.cars[item]

    def __repr__(self):             # same as to_string in JAVA ( more priority than __str__ ) . # if u define this method in a class , it enables the printing its object.
        return f'<Garage {self.cars}'
"""
    def __str__(self):              # same as to_string in JAVA , if defined it takes priority over __repr__
        return f'Garage with {len(self.cars)} cars'
"""
class Factory:
    def __init__(self):
        self.products = []

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        return self.products[item]

    def __repr__(self):             # same as to_string in JAVA ( more priority than __str__ )
        return f'<Factory {self.products}'
"""
    def __str__(self):              # same as to_string in JAVA
        return f'Factory with {len(self.cars)} cars'
"""

ford = Garage()
ford.cars.append("Explorer")
ford.cars.append("Bronco")

print(f"ford[0]:{ford[0]}") # calls __getitem__ internally
print(f"Garage.__getitem__(ford,0):{Garage.__getitem__(ford,0)}")
print(f"ford:{ford}") # is __str__ is defined it will print else will call __repr__ , comment __str__ and test.

print("What Type of Object is ford:{}".format(ford.__class__)) # displayes the Class Type the object ford belongs to.

movie= ["a","b","c"]
print("What Type of Object is movie:{}".format(movie.__class__)) # displayes the Class Type the object ford belongs to.

factory = Factory()
factory.products.append("Prod1")
factory.products.append("Prod2")
print("What Type of Object is factory:{}".format(factory.__class__)) # displayes the Class Type the object ford belongs to.
print("Length of factory obj:{}".format(len(factory))) # displayes the Class Type the object ford belongs to.

print("Iterating over ford & factory objects")
# Now I can iterate over the objects Garage & Factory as thy are now supported by __getitem__
for idx,car in enumerate(ford):
    print("Car#{} of ford:{}".format(idx,car))
for idx,car in enumerate(factory):
    print("Prod#{} of ford:{}".format(idx,car))