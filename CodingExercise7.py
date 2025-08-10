

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for i in range(1,101):
    factor3 = i % 3
    factor5 = i % 5
    if factor3 == 0 and factor5 == 0 :
        print("FizzBuzz")
    elif factor3 == 0:
        print("Fizz")
    elif factor5 == 0:
        print("Buzz")
    else:
        print(i)