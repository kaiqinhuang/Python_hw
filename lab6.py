"""
lab6

Name: Kaiqin Huang
Date: 1/11/2017

A module of functions factorial and cartesian product.
"""

def factorial(n):
    """Gets the factorial of n
        
    Args:
        n: Maximum number of the factorial
        
    Returns:
        integer: The factorial of n
    """
    
    fac = 1
    
    for i in range(n):
        fac *= i+1
    
    return fac
        
def cartesian(list1,list2):
    """Gets the Cartesian Product of two lists
        
    Args:
        list1 and list2: Any two lists of strings, integers, or any other types.
        
    Returns:
        list: Print out the list of Cartesian Product of the two given lists.
    """

    outputs = []
    
    for x in list1:
        for y in list2:
            outputs.append((x,y))

    print(outputs)
