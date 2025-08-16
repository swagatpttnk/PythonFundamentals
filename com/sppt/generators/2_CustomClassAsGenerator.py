class FirstHunderedGenerator:
    def __init__(self, bound):
        self.number = 0
        self.bound = bound

    def __next__(self):         # in Python3 it is __next__() , in prior version it is next()
        if self.number < self.bound:
            current = self.number
            self.number = self.number + 1
            return current
        else:
            raise StopIteration()


mygen = FirstHunderedGenerator(3)
print(f' First iteration:{next(mygen)}')
print(f' 2nd iteration:{next(mygen)}')
print(f' 3rd iteration:{next(mygen)}')

for i in mygen:
    print(f'value:{i}')                 #<-- TypeError: 'FirstHunderedGenerator' object is not iterable
