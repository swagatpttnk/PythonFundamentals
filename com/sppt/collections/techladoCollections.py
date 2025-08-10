class CollectionDemo:
    def __init__(self):
        pass

    def demo_lists(self):
        # Sets
        print("In demo_lists Method....")
        list_friends1 = ["Ravi", "Sam", "putin"]
        list_friends2 = ["Meethi", 2, "Nick"]
        list_friends3 = [["Meethi", 21], ["Steve", 2], ["Nick", 4]]
        print("list_friends1:{}".format(list_friends1))
        print("list_friends2:{}".format(list_friends2))
        print(list_friends2)
        print("First item of List list_friends1:{}".format(list_friends1[0]))
        print("2nd item of List list_friends2:{}".format(list_friends2[1]))
        print("2nd item's 1st element of List list_friends3:{}".format(list_friends3[1][0]))
        list_friends1.append("Dan")
        print("After Appending an item to List list_friends1:{}".format(list_friends1))
        list_friends1.remove("Dan")
        print("After Removing an item to List list_friends1:{}".format(list_friends1))
        print("Popping an item from List list_friends1:{}".format(list_friends1.pop()))
        print("After Popping an item from List list_friends1:{}".format(list_friends1))
        print("Size of List list_friends1:{}".format(len(list_friends1)))
        # methods on list
        grades = [23, 45, 67, 87]
        total = sum(grades)
        length = len(grades)
        average = total / length
        print("### average:{}".format(average))

        # Join
        print("### All firends1:{}".format("|".join(list_friends1)))

    def quiz3(self):
        lottery_numbers = {13, 21, 22, 5, 8}

        """
        A player looks like this:

        {
            'name': 'PLAYER1',
            'numbers': {1, 2, 3, 4, 5}
        }

        Define a list with two players (you can come up with their names and numbers).
        """

        players = [{
            'name': 'PLAYER1',
            'numbers': {1, 2, 13, 4, 5}
        },
            {
                'name': 'PLAYER2',
                'numbers': {1, 22, 3, 8, 5}
            }]

        """
        For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
        Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
        You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
        Then construct a string and print it out.

        Remember: the string must contain the player's name and the amount of numbers they got right!
        """
        for player in players:
            print(
                "Player {} has won {} numbers right".format(player["name"], len(lottery_numbers.intersection(player["numbers"]))))

    def demo_tuple(self):
        # tuple
        print("In demo_tuple Method....")
        not_a_tuple = "test"
        is_a_tuple = "test",  # <--- notice the comma at the end
        tuple_friends = "Dev", "Eva", "Ron"
        tuple_friends2 = ("Ravi", "Sam", "putin")  # <---a it clearer with brackets
        print("tuple_friends:{}".format(tuple_friends))
        # Accessing tupple
        print("2nd element in tuple_friends:{}".format(tuple_friends[1]))
        # adding or removing to/from tuple
        # tuple_friends.append() <-- doesnt works as they are IMMUTABLE
        # Work around for adding removing
        tuple_friends3 = tuple_friends + (
            "Flora",)  # <--- creates new tuple named tuple_friends3 but tuple_friends & ("Flora",) are not changed
        print(" element in tuple_friends3:{}".format(tuple_friends3))

    def demo_sets(self):
        # Sets - No order & no duplicates
        print("In demo_sets Method....")
        set_friends1 = {"Ravi", "Sam", "putin"}
        set_friends2 = {"Meethi", "Sam", "Nick"}
        print("set_friends1:{}".format(set_friends1))
        print("set_friends2:{}".format(set_friends2))

        # Adding/removing
        set_friends1.add("Jen")
        set_friends2.add("Meethi")
        print("After adding to set_friends1: {}".format(set_friends1))
        print("After adding to set_friends2: {}".format(set_friends2))
        print("Size of set_friends2: {}".format(len(set_friends2)))

        print("Union of set_friends1 & set_friends2:{}".format(set_friends1.union(set_friends2)))
        print("Intersection of set_friends1 & set_friends2:{}".format(set_friends1.intersection(set_friends2)))
        print("Difference of set_friends1 & set_friends2:{}".format(set_friends1.difference(set_friends2)))
        print("Difference of set_friends2 & set_friends1:{}".format(set_friends2.difference(set_friends1)))
        print("Symetric Difference of set_friends1 & set_friends2:{}".format(
            set_friends1.symmetric_difference(set_friends2)))
        print("Symetric Difference of set_friends2 & set_friends1:{}".format(
            set_friends2.symmetric_difference(set_friends1)))

    def demo_dictionary(self):
        print("In demo_dictionary Method....")
        friends_age = {"Swagat": 41, "Ron": 2, "Jim": 34, "Mira": "Forty",
                       "Complex": {"SetItem1", "SetItem2", "SetItem2"},
                       22: "axe", 22: "fer"}
        print("All Friends age:{}".format(friends_age))
        print("Swagat's age is :{}".format(friends_age["Swagat"]))
        print("Mira's age is :{}".format(friends_age["Mira"]))
        print("Complex's content :{}".format(friends_age["Complex"]))
        print("22's content :{}".format(friends_age[22]))

        # adding to dictionary
        friends_age["Kevin"] = 43
        print("All Friends age:{}".format(friends_age))
        # removing from dictionary - using del
        del friends_age["Kevin"]
        print("All Friends age:{}".format(friends_age))

        friends_age["Kevin"] = 54  # adding it back
        print("All Friends age ,adding back Kevin:{}".format(friends_age))

        # removing from dictionary - using pop
        kevin_age = friends_age.pop("Kevin")
        print("Kevin's age:{}".format(kevin_age))
        print("All Friends age after removing Kevin:{}".format(friends_age))

        kevin_age = friends_age.pop("Kevin", None)
        print("Kevin's age (from popping):{}".format(kevin_age))
        print("All Friends age after removing Kevin again:{}".format(kevin_age))

        x = friends_age.popitem()
        print("All Friends age -popitem1:{}".format(friends_age))
        x = friends_age.popitem()
        print("All Friends age -popitem2:{}".format(friends_age))

    def demo_mixedCollection(self):
        print("In demo_mixedCollection Method....")
        friends = ({"name": "Swagat", "age": 44},
                   {"name": "Annie", "age": 34},
                   {"name": "Kitty", "age": 14},
                   {"name": "Meethi", "age": 4}
                   )
        friend = friends[1]
        print("Style1:  friends[1][\"name\"]:{}".format(friends[1]["name"]))
        print("Style2:  friend = friends[1] -> friend[\"name\"]:{}".format(friend["name"]))
        ## interconversion
        # convert list of tuples --> dictionary
        col_friends = [("rolf", 24), ("Adam", 34), ("Jenny", 54)]
        col_friends_dict = dict(col_friends)
        print("col_friends:{}".format(col_friends))
        print("col_friends_dict:{}".format(col_friends_dict))


if __name__ == "__main__":
    demo = CollectionDemo()
    demo.demo_lists()
    # demo.quiz3()
    # demo.demo_tuple()
    # demo.demo_sets()
    # demo.demo_dictionary()
    # demo.demo_mixedCollection()

