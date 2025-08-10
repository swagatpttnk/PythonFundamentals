
class SlicingDemo:
    def __init__(self):
        pass


    def slicing_demo(self):
        # https://blog.teclado.com/python-slices/
        # https://blog.teclado.com/python-slices-part-2/
        # https://blog.teclado.com/python-quick-sequence-reversal/

        friends = ["Annie", "Sppt", "Gary", "Olam", "Robin", "Obama"]
        #         [ 0         1        2       3        4        5   ] # length = 6
        #         [-6        -5       -4      -3       -2       -1   ] # length = 6
        print(f"friends: {friends}")
        print(f"len(friends): {len(friends)}")
        print(f"friends[2:4]: {friends[2:4]}")  # starts at 2( included), ends at 4 ( excluded )
        print(f"friends[2:]: {friends[2:]}")  # starts at 2( included), ends at len(friends) ( excluded )
        print(f"friends[:3]: {friends[:3]}")  # starts at 0( included), ends at 3 ( excluded )

        print(f"friends[2:len(friends)]: {friends[2:len(friends)]}")  # starts at 2 (included), ends at len(friends) (excluded)
        print(f"friends[2:9]: {friends[2:9]}")  # starts at 2( included), ends at 9
        # ( No arrayIndexOutOfBound , will print from 2 to len(friends))
        print(f"friends[-2:]: {friends[-2:]}")  # starts at -2( included), ends at len(friends)
        print(f"friends[-2:-4]: {friends[-2:-4]}")  # starts at -2( included), ends at -4 ( excluded ), cant traverse right2left
        print(f"friends[-3:-1]: {friends[-3:-1]}")  # can traverse left2Right always
        print(f"friends[-3:-1]: {friends[-3:-1]}")  # starts at -3( included), ends at -1 ( excluded )
        print(f"friends[:-3]: {friends[:-3]}")  # starts at 0( included), ends at -3 ( excluded )