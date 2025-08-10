class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    def from_sum(self, value):  # Instance method , takes self as 1st parameter
        return FixedFloat(self.amount + value)

    @staticmethod
    def from_sum_staticmethod(value1, value2):  # Static method , doesn't take self or class as 1st parameter
        return FixedFloat(value1 + value2)

    @classmethod
    def from_sum_classmethod(clss, value1, value2): # Class method , takes class as 1st parameter
        return clss(value1 + value2)


number = FixedFloat(29.3)
print(f"FixedFloat :{number}")
new_number = number.from_sum(10.0)
print(f"FixedFloat from_sum:{number}")


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'EURO {self.symbol}{self.amount:.2f}'


euro = Euro(223.0)
print(f"Euro :{euro}")
euro = Euro.from_sum_staticmethod(223.0, 10)
print(f"Euro from_sum_staticmethod:{euro}")
euro = Euro.from_sum_classmethod(223.0, 10)
print(f"Euro from_sum_classmethod:{euro}")

# Always recommended to use class method in place of static method
"""
When to Choose Which:

Use a regular (instance) method: If your method needs to access or modify instance-specific data (i.e., it needs self). This is the most common type of method.
Use a @classmethod: If your method needs to access or modify class-level attributes, or if it needs to create an instance of the class (like an alternative constructor), especially when you want this behavior to be polymorphic across subclasses.
Use a @staticmethod: If your method doesn't need access to instance data (self) or class data (cls), but it logically belongs to the class for organizational purposes. If it doesn't fit here, consider if it should just be a standalone function outside the class.
"""