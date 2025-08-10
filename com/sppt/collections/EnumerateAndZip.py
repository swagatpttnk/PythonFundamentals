"""
Enumeration fnctions :
The enumerate(list) function in Python adds a counter to an iterable, returning both the index and the element
during iteration. It is particularly useful when you need to loop through an iterable and keep track of the index.
"""


class EnumerateAndZipDemo:
    def __init__(self):
        pass

    def demo_enumerate_zip(self):
        friends = ["Annie", "Sppt", "Gary"]

        # without enumerate
        print("=== Without enumerate function====")
        counter = 0

        for friend in friends:
            print(f"counter ={counter} , friend :{friend}")
            counter += 1

        print("=== With enumerate function====")
        for cntr, friend in enumerate(friends):
            print(f"counter ={cntr} , friend :{friend}")

        print("=== Passing enumerate to list ====")
        print(list(enumerate(friends)))
        print("----*** Using zip to get the same result ---***")
        print(list(zip([0, 1, 2, 3, 4, 5], friends)))
        print("=== Passing enumerate to dict ====")
        print(dict(enumerate(friends)))
