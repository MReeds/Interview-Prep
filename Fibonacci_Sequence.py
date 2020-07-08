"""Basic Fibonacci Sequence"""

# 'i' = each index in the range of 0 through 10
# the loop will occur for the amount of times declared in the range
# 'a,b' is reassigned in the loop to equal:
# 'a' (which is whatever 'b' currently is in the loop) and 'b' as 'a' + 'b'

a,b = 0,1
for i in range(0, 10):
    print(a)
    a,b = b, a+b
    


"""Fibonacci Generator"""

# Before loop, 'a' equals user input number
# 'b' equals "generator object fib" which calls fib()
# Once b.next() is called to loop through i in range of 'a' ... 'a', 'b' = 0, 1

# We use the next() function to manually iterate through all the items of an iterator. 
# When we reach the end and there is no more data to be returned,
# it will raise the StopIteration Exception

a = int(input('Give amount: '))

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

b = fib()
b.__next__()

for i in range(a):
    print(b.__next__())
