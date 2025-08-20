def starts_with_r_fun(friend, char):
    return friend.upper().startswith(char.upper())


friends = ["Rolf", "Randy", "Kevin", "Gons"]
generator_starts_with_r = filter(lambda x: starts_with_r_fun(x, "R"),
                                 friends)  # arg1: a pedicate function , arg2:iterable
generator_starts_with_k = filter(lambda x: starts_with_r_fun(x, "K"),
                                 friends)  # arg1: a pedicate function , arg2:iterable

# filter function returns a Iterable generator , so calling for & list on them will return values
for f in generator_starts_with_r:
    print(f'friend starting with r:{f} ')

print(f'friend list with k:{list(generator_starts_with_k)} ')  # <-- returns value
print(
    f'friend list with k:{list(generator_starts_with_k)} ')  # <-- returns no value as it automatically checks the StopIteration exception & returns empty []

another_generator_starts_with_k = (f for f in friends if f.startswith('K') )
print(f' another_generator_starts_with_k:{list(another_generator_starts_with_k)}')

"""
another_generator_starts_with_k  is same as generator_starts_with_k but the performance of 
another_generator_starts_with_k is better than generator_starts_with_k due to need of filter function.
filter function is more readable than generator comprehension .
We can write this filter as a custom function as shown below :
"""


def my_custom_filter(func, iterable,char):
    for i in iterable:
        if func(i,char):
            yield i


c_generator_starts_with_r = my_custom_filter(lambda x,y: starts_with_r_fun(x, y),
                                           friends,"K")
for f in c_generator_starts_with_r:
    print(f'c_generator_starts_with_r:{f} ')