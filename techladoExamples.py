import techladoBoolean
from com.sppt.collections import techladoCollections
from com.sppt.collections.EnumerateAndZip import EnumerateAndZipDemo
from com.sppt.collections.Slicing import SlicingDemo
from com.sppt.errorhandling.BasicExceptionHandlingDemo import BasicExceptionHandling
# from com.sppt.flowcontrol import techladoFlowControl
from com.sppt.flowcontrol.techladoFlowControl import FlowControlDemo
from com.sppt.collections.Comprehensions_List import ComprehensionsList
from com.sppt.collections.Comprehensions_Set import ComprehensionsSet
from com.sppt.collections.Comprehensions_Dictionary import ComprehensionsDictionary
from com.sppt.database.app import DatabaseDemo


class TechDemo:
    def __init__(self):
        pass

    def demo_user_input(self):
        # Python String  Formatting
        age = input("Enter your Age:")
        print(
            f"Your Age in Months is : {age * 12}")  # <----- prints age 12 times i.e if age=2 .... prints : 222222222222
        age_num = int(age)
        print(f"Sorry , Your Age in Months is : {age_num * 12}")

    def using_default_value(self):
        default_greeting = "there"
        name = input("please enter your name : (optional)")
        username = name or default_greeting
        print(f"Hello, {username}")


if __name__ == "__main__":
    # demo = TechDemo()
    # demo.demo_user_input()
    # demo.using_default_value()

    # demo = techladoCollections.CollectionDemo()
    # demo.demo_dictionary()

    # demoBoolean = techladoBoolean.BooleanDemo()
    # demoBoolean.boolean_comparison()
    # demoBoolean.boolean_evaluation()

    # demo = FlowControlDemo()
    # demo.demo_if_else()
    # demo.demo_while()
    # demo.demo_do_while()
    # demo.demo_for()

    # demo = ComprehensionsList()
    # demo.demo_listComprehension()
    # demo.demo_listComprehension_withCondition()

    # demo = ComprehensionsSet()
    # demo.demo_sets_comprehension()

    # demo = ComprehensionsDictionary()
    # demo.demo_dictionary_comprehension()

    # demo = EnumerateAndZipDemo()
    # demo.demo_enumerate_zip()

    # demo=SlicingDemo()
    # demo.slicing_demo()

    # demo = BasicExceptionHandling()
    # demo.demo_exception_handling()

    demo = DatabaseDemo()
    demo.menu()
