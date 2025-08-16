class PrimeGeneratorIterator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:  # not prime
                    break
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator


class PrimegeneratorIterable:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return PrimeGeneratorIterator(self.stop)


class PrimeGeneratorIteratorAndIterable:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:  # not prime
                    break
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator

    def __iter__(self):
        return self


class AnotherIterable:           # this class is also a iterator i.e a class having __len__ & __getitem__ is also an iterator
    def __init__(self):
        self.cars = ["Fieasta", "Bronco", "Mustang"]


    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


mygen = PrimeGeneratorIterator(20)
print(f' First iteration:{next(mygen)}')
print(f' 2nd iteration:{next(mygen)}')
print(f' 3rd iteration:{next(mygen)}')

"""
for i in mygen:
    print(f'value:{i}')  # <-- TypeError: 'FirstHunderedGenerator' object is not iterable
"""
mygeniterable = PrimegeneratorIterable(10)
for i in mygeniterable:
    print(f'mygeniterable value:{i}')

mygenboth = PrimeGeneratorIteratorAndIterable(7)
for i in mygenboth:
    print(f'mygenboth value:{i}')

for car in AnotherIterable():
    print(f'AnotherIterable :{car}')