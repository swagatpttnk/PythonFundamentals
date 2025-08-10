# LIST COMPREHENSION  is a feature of Python that enables us to create new Lists from existing Lists or scratch

class ComprehensionsList:

    def __init__(self):
        pass
    def demo_listComprehension(self):
        numbers = [0, 1, 2, 3, 4, 5]
        #         [ 0         1        2       3        4        5   ] # length = 6
        #         [-6        -5       -4      -3       -2       -1   ] # length = 6
        double_numbers = []
        for num in numbers:
            double_numbers.append(num * 2)
        print(f"numbers:{numbers}")
        print(f"double_numbers:{double_numbers}")

        # using comprehension
        double_numbers_compr = [num * 2 for num in numbers]
        print(f"double_numbers_using_comprehension:{double_numbers_compr}")

        double_numbers_compr = [5 for _ in numbers]  # _ signals that you dont care about the intermittent value
        print(f"double_numbers_compr constant output:{double_numbers_compr}")

        age_str = [f"Age of my friend is {age}" for age in numbers]
        print(f"age_str:{age_str}")

        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        friends_lowercase = [friend.lower() for friend in friends]
        print(f"friends:{friends}")
        print(f"friends_lowercase:{friends_lowercase}")
        friend = input("Input your friend name:")
        if friend.lower() in friends_lowercase:
            print(f"Yes {friend} is on of your Friends")
        else:
            print(f"I dont know any of your friends named {friend}")

    def demo_listComprehension_withCondition(self):
        # Comprehension with Conditions
        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        friends_lowercase = [friend.lower() for friend in friends]
        guests = ["Ashok", "Sppt", "Siva", "Olam", "Anand"]
        # Aim: to find All guests that is a friend

        # Style 1 : convert friends & guests to set of lowercase strings & find their intersection
        friends_lowercase_set = set(friends_lowercase)
        guests_lowercase_set = set(guest.lower() for guest in guests)
        guest_thatare_friends = friends_lowercase_set.intersection(guests_lowercase_set)
        print(f"SetStyle:Guests that are Friends are:{guest_thatare_friends} ")
        # Style 2 : use comprehension
        guest_thatare_friends_comprehension = [
            guest.title()           # <--- new thing that u want to put in the list
            for guest in guests     # <--- iteration
            if guest.lower() in friends_lowercase  # <-- condition # dont replace n friends_lowercase
        ]
        """ The above comprehension can also be replaced expanded line for friends_lowercase , but it is not readable,thus
        not recommended
        guest_thatare_friends_comprehension = [
            guest.title() 
            for guest in guests 
            if guest.lower() in friend.lower() for friend in friends #  friends_lowercase expanded to 'friend.lower() for friend in friends'
        ]
        """

        print(f"ComprehensionStyle:Guests that are Friends are:{guest_thatare_friends_comprehension} ")


