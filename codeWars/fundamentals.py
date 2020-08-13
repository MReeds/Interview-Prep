# A string is considered to be in title case if each word in the string 
# is either (a) capitalised (that is, only the first letter of the word 
# is in upper case) or (b) considered to be an exception and put entirely 
# into lower case unless it is the first word, which is always capitalised.

# Write a function that will convert a string into title case, given an 
# optional list of exceptions (minor words). The list of minor words will 
# be given as a string with each word separated by a space. Your function 
# should ignore the case of the minor words string -- it should behave in 
# the same way even if the case of the minor word string is changed.

# Arguments

# First argument: space-delimited list of minor words that must always be 
# lowercase except for the first word in the string.
# Second argument: the original string to be converted.

def title_case(title, minor_words=''):
    '''Converts string into title case given an optional list of exceptions
    minor words will be given as a string with each word seperated by a space.'''
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])



# Write a function that takes an array of numbers (integers for the tests)
# and a target number. It should find two different items in the array that,
# when added together, give the target value. The indices of these items 
# should then be returned in a tuple like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; 
# any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or 
# greater, and all of the items will be numbers; target will always be the 
# sum of two different items from that array).

def two_sum(numbers, target):
    '''Takes array of nums and a target num. Returns two ints that added together 
    equal the target num'''
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j) and (numbers[i] + numbers[j] == target):
                return [i, j]