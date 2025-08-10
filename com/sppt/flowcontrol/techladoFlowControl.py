class FlowControlDemo:
    def __init__(self):
        pass

    def demo_if_else(self):
        # if,elif,else ----------
        print("---- Entered DemoIfElse ------")
        wife_name="Annie"
        user_name = input("Input username :")
        friends = ["a", "b", "c"]
        family = ["d", "e", "f"]
        if user_name in friends:
            print(f"Hello Friend, {user_name}")
        elif user_name in family:
            print(f"Hello Family, {user_name}")
        elif user_name == wife_name:
            print(f"It's your Wife {user_name}, please Run  .. :) ")
        else:
            print(f"Hello Stranger, {user_name}")

        print("---- Exiting DemoIfElse ------")

    def demo_while(self):
        user_input = input("Please input 'p' to print & 'q' to quit:")
        while (user_input != 'q'):
            print("Hello")
            user_input = input("Please input 'p' to print & 'q' to quit:")
    def demo_do_while(self):
        while True:
            user_input = input("Please input 'p' to print & 'q' to quit:")
            if(user_input == 'q'):
                break;
            else:
                print("Hello")

    def demo_for(self):
        # Print out numbers from 1 to 100 (including 100).
        # But, instead of printing multiples of 3, print "Fizz"
        # Instead of printing multiples of 5, print "Buzz"
        # Instead of printing multiples of both 3 and 5, print "FizzBuzz".

        for num in range(1, 101):
            if (num % 3 == 0 and num % 5 == 0):
                print("FizzBuzz")
            elif (num % 3 == 0):
                print("Fizz")
            elif (num % 5 == 0):
                print("Buzz")
            else:
                print(num)


if __name__ == "__main__":
    demo = FlowControlDemo()
    #demo.demo_if_else()
    #demo.demo_while()
    #demo.demo_do_while()
    #demo.demo_for()
