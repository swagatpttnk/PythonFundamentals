
class ComprehensionsSet:
    def __init__(self):
        pass

    def demo_sets_comprehension(self):
        # Set comprehensions
        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        guests = ["Ashok", "Sppt", "Siva", "Olam", "Anand"]

        friends_lower = { n.lower() for n in friends}
        guests_lower = { n.lower() for n in guests}

        present_friends = friends_lower.intersection(guests_lower)
        present_friends = { n.title() for n in present_friends}
        print(f"present_friends:{present_friends}")