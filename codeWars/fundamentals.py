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
            
            
# The museum of incredible dull things wants to get rid of some exhibitions. 
# Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. 
# She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibitions, she's off to an important fair, 
# so she asks you to write a program that tells her the ratings of the items after one 
# removed the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
# If there are multiple elements with the same value, remove the one with a lower index. 
# If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.
def rmv_smallest(numbers):
    if len(numbers) <= 1: return []
        numbers.remove(min(numbers))
        return numbers
    
    
# Make sure that k is greater than zero and less than the
    # length of the array of strings. Otherwise return an empty string
    if k <= 0 or k > len(strarr):
        return ''

    # Finding the longest string consisting of k consecutive
    # strings is equivalent to finding the maximum sum of
    # k consecutive elements of an array that represents the
    # lengths of an array of strings.

    # star_lengths represents a list of lengths of the initial
    # array of strings.
    starr_lengths = list(map(len, strarr))
    # Find the maximum sum of k consecutive elements
    # requires keeping a temperary maximum length.
    temp_max_len = 0
    # We also need to keep the position of the first element of
    # each group.
    position = 0

    # Scan the whole list of lengths except the final k elements
    for p in range(len(starr_lengths) - (k - 1)):
        # We need to find the sum of the current set of elements
        # starting at position p
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p+i]
        
        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position+k]])

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
        
        
        
        
# The main idea is to count all the occurring characters in a string. If you have a string like aba, 
# then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    if string=="":
        return {}
    else:
        dict={}
        for i in string:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        return dict
    
# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
def remove_url_anchor(url):
    splt = url.split('#',1)
    sub = splt[0]
    return sub

# Refactored method
def remove_url_anchor(url):
    return url.partition('#')[0]

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
def solution(string, ending):
    return string.endswith(ending)
