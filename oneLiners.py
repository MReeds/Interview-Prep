from functools import reduce
from itertools import combinations

""" Swapping variables """

a = 'dog'
b = 'cat'

a,b = b,a

# print('a', a, 'b', b)

""" List Comprehension """
sqrs = [x*x for x in range(11)]
# print(sqrs)

""" Subset of a set"""

print(list(combinations(range(1, 4), 2)))
