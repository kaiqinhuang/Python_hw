"""
lab8.py

Name: Kaiqin Huang
Date: 1/17/2017

A module of functions count_merge(), count_as(), and split_evens().
"""


def count_merge(set1, set2):
    '''Merges two sets and returns the length of the new set
        
        Args:
            set1 and set2: Two sets
        
        Returns:
            len: The length of the merged set
    '''
    
    my_set = set1
    my_set_new = my_set.union(set2)
    return len(my_set_new)


def count_as(string_list):
    '''Counts how many times lower case letter "a" appears in the string list
        
        Args:
            string_list: A list of strings
        
        Returns:
            num_as: Counter of how many times letter "a" appears
    '''

    num_as = 0
    
    for s in string_list:
        num_as += s.count("a")

    return num_as


def split_evens(int_list):
    '''Splits an integer list into an even number list and a odd number list
        
        Args:
            int_list: A list of integers
        
        Returns:
            even_list: A list of even numbers in the given integer list
            odd_list: A list of odd numbers in the given integer list
    '''
    
    even_list = []
    odd_list = []

    for i in int_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return (even_list, odd_list)

