""" Comprehensions in Python provide us with a short and concise way 
    to construct new sequences (such as lists, set, dictionary etc.) 
    using sequences which have been already defined"""

# Create a new list of squared numbers from the original list 

original_list = [1,2,3,4,5,6,7,8,9]

squared = [num*num for num in original_list]
# print(squared)


# l is the list of all numbers 2 times n where n is an item 
# in the (0, 1, 2) tuple, for which tuple element is greater than zero.

i = [2 * n for n in (0,1,2) if n > 0]
# print(i)

# Print only odd numbers in the list
odd = [num for num in [1, 2, 3, 4, 6, 8, 10, 12, 13, 17, 20, 22, 35, 27, 32, 47] if num % 2]
# print(odd)

my_list = [[m,n] for m in (5,6) for n in (3,4)]
# print(my_list)