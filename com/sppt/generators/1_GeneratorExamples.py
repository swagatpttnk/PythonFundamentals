class GeneratorDemo:
    def count_up_to(self, max_num):
        """
        A simple generator function that yields numbers from 1 up to max_num.
        """
        n = 1
        while n <= max_num:
            yield n  # This is where the function yields a value and pauses
            n += 1

    def simple_generator(self):
        yield 1
        yield 2
        yield 3

    def prime_generator(self, bound):
        for n in range(2, bound):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                yield n


if __name__ == "__main__":
    demo = GeneratorDemo()
    my_counter = demo.count_up_to(5)
    print("First call to next():", next(my_counter))  # Output: First call to next(): 1
    print("Second call to next():", next(my_counter))  # Output: Second call to next(): 2

    for count in my_counter:
        print(
            f" item:{count}")  # -- the loop stops automatically & doesn't throws exception when the generator exhausts

    my_counter = demo.count_up_to(5)
    print(f"---printing count_uo_to generator with list after 1st 2 elements---")
    print("First call to next():", next(my_counter))  # Output: First call to next(): 1
    print("Second call to next():", next(my_counter))  # Output: Second call to next(): 2
    print(list(my_counter))
    """"  ------Using try-except StopIteration with next():-------- """
    my_gen = demo.simple_generator()

    try:
        first_item = next(my_gen)
        print(f"Got item: {first_item}")  # Output: Got item: 1
        # At this point, the generator has advanced.

        second_item = next(my_gen)
        print(f"Got item: {second_item}")  # Output: Got item: 2

        # Let's try to get the next one and see if it exhausts
        print("Attempting to get the third item...")
        third_item = next(my_gen)
        print(f"Got item: {third_item}")  # Output: Got item: 3

        print("Attempting to get the fourth item (will exhaust)...")
        fourth_item = next(my_gen)  # This will raise StopIteration
        print(f"Got item: {fourth_item}")

    except StopIteration:
        print("Generator is exhausted!")  # Output: Generator is exhausted!

    print("Program continues after exhaustion handling.")

    """" ------- """
    p = demo.prime_generator(10)

    print(f" NEXT prime_generator:{next(p)}")
    print(list(p))
