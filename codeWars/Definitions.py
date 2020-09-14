# Higher Order Funcitons
# A function is called Higher Order Function if it contains other functions as a parameter 
# or returns a function as an output i.e, the functions that operate with another function 
# are known as Higher order Functions. It is worth knowing that this higher order function 
# is applicable for functions and methods as well that takes functions as a parameter or returns 
# a function as a result. Python too supports the concepts of higher order functions.

# Python program to illustrate functions can be treated as objects  
def shout(text):  
    return text.upper()  
    
print(shout('Hello'))  
    
# Assigning function to a variable 
yell = shout  
    
print(yell('Hello'))
