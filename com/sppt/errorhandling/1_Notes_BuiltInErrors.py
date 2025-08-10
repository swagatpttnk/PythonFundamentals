"""
How to Do Error Handling in General :
1.Look at your code
2.Put the Error & message in Google : see if something comes up in StackOverFlow
3.Look at your code slowly & try to identify the source of error .
4.Run some part of your of the code in isolation to confirm your doubt.
5.Use a debugger in the IDE .
Types Of Error In Python:

IndexError : When we try to access an index that doesn't exist in the list .same as ArrayIndexOutOfBounds in Java
KeyError : When we try to access value for a key from a Dictionary and the key doesn't exist.
NameError : When we try to read a variable hat is not yet declared or written .
AttributeError :When we try to access a method or property of an object that  doesn't exist. Ex Accessing .intersection() on List.
NotImplementedError: Same as AttributeError but used for user defined classes Developer must throw this error to indicate
                        that the feature/method is under development.Ref: https://docs.python.org/3/library/exceptions.html#NotImplementedError
RuntimeError :Base class of all the errors .
SyntaxError : Syntax related . missing colon or no def key word etc.
IndentationError :
    def add(x,y):
    return x + y; <--- incorrect indentation.

    def add(x,y):
        return x + y <--- correct

    def add(x,y):
        pass
    return x + y <--- indentation OK but x,y are not defined outside the program but read to add them, throws NameError

TabError : Occurs when we switch editors or mix n match tab & spaces .
TypeError : When we mix incompatible types , int + str for example .
ValueError : When we mix incompatible values , int(3.5) <-- passing float to int. Mostly built-in functions throws this .
ImportError : Throws when circular imports happens between 2 or more files .
DeprecatingWarning : When methods gets deprecated .

"""