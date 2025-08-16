import itertools

def finite_sequence_generator():
    yield "apple"
    yield "banana"
    yield "cherry"

# Create a generator object
my_gen = finite_sequence_generator()

# Use itertools.tee to create two independent iterators from my_gen
# my_gen_peek will be used to check for the next item
# my_gen_actual will be used for normal iteration
my_gen_actual, my_gen_peek = itertools.tee(my_gen, 2)

print("Starting iteration...")

while True:
    try:
        # Try to get the next item using the 'peek' iterator
        # This will advance my_gen_peek
        peeked_item = next(my_gen_peek)
        print(f"  (Peeked ahead: '{peeked_item}')") # We know there's a next item

        # Now get the actual item using the 'actual' iterator
        # This will advance my_gen_actual
        current_item = next(my_gen_actual)
        print(f"Processing: '{current_item}'")

        # You could add logic here based on 'peeked_item'
        # For example, if peeked_item is the last one you care about, break.

    except StopIteration:
        print("Generator exhausted. No more items to process.")
        break

print("Finished.")
