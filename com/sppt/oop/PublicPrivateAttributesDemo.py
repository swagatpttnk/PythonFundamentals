class MyClass:
    def __init__(self, value):
        self.__private_attribute = value * 3 # Name mangled: private attribute

    def public_method(self):
        print("This is a public method.")
        self.__private_method() # It's fine to call the mangled method from inside the class

    def __private_method(self): # Name mangled: private method
        print("This is a private method (by name mangling).")
        print(f"Private attribute value: {self.__private_attribute}")


if __name__ == "__main__":
    # Using the class
    obj = MyClass(20)

    # Accessing public members (normal)
    obj.public_method()

    # Trying to access private members directly (will fail)
    try:
        print(obj.__private_attribute)
    except AttributeError as e:
        print(f"Error trying to access __private_attribute directly: {e}")

    try:
        obj.__private_method()
    except AttributeError as e:
        print(f"Error trying to call __private_method directly: {e}")

    # Accessing private members using the mangled name (possible, but don't do this!)
    print(obj._MyClass__private_attribute) # You CAN access it if you know the mangled name
    obj._MyClass__private_method()      # You CAN call it if you know the mangled name
