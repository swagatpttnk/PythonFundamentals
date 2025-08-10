class BooleanDemo:
    def __init__(self):
        pass

    def boolean_comparison(self):
        # Boolean comparison in Python
        var1 = True
        var2 = False  # <--- not false , its capital F
        age = int(input("enter ur age :"))
        if (age >= 18):
            print("you are eligible to vote..")
        else:
            print("you are NOT eligible to vote..")

    def boolean_evaluation(self):

        # ------------ boolean evaluation -----
        bool0 = bool(0)
        print(f"bool(0):{bool0}")
        bool5 = bool(5)
        print(f"bool(5):{bool5}")
        boolAnyStr = bool("Abcds")
        print(f"bool(boolAnyStr):{boolAnyStr}")
        boolEmptyStr = bool("")
        print(f"bool(boolEmptyStr):{boolEmptyStr}")

        if(5):
            print("5 as boolean is always {}".format(str(True)))
        if (0):
            print("0 as boolean is always {}".format(str(False)))

        condition = bool(5)
        if (condition):
            print("5 as boolean is always {}".format(str(True)))
        else :
            print("0 as boolean is always {}".format(str(False)))

        condition = bool(0)
        if (condition):
            print("5 as boolean is always {}".format(str(True)))
        else :
            print("0 as boolean is always {}".format(str(False)))