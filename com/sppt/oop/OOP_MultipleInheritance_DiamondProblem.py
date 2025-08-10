class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C): # Inherits from B first, then C
    pass

class E(C, B): # Inherits from C first, then B
    pass

print("MRO for D:", D.mro())
# Output: MRO for D: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

print("MRO for E:", E.mro())
# Output: MRO for E: [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

d_obj = D()
d_obj.greet() # Output: Hello from B (because B comes before C in D's MRO)

e_obj = E()
e_obj.greet() # Output: Hello from C (because C comes before B in E's MRO)
