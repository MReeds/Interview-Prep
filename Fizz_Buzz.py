# For multiples of five (5, 10, 15, etc.) 
# print "Fizz" instead of the number.
# For the multiples of seven (7, 14, 21, etc.)
# print "Buzz".
# For numbers which are multiples of both five 
# and seven print "FizzBuzz".
# To determine if a number can be evenly divided
# by 5 or 7, use the Python modulo operator.

"""Creating and calling a function"""

def fizz_buzz():
    for num in range(1, 101):
        if(num % 5 == 0 and num % 7 == 0):
            print("FizzBuzz")
        elif(num % 5 == 0):
            print("Fizz")
        elif(num % 7 == 0):
            print("Buzz")
        else:
            print(num)
fizz_buzz()