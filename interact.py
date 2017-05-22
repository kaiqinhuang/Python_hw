"""
interact

A module of common functions for interacting with users.
"""

def get_list_of(name_of_thing = "thing"):
    """Gets a list of things from the user

    Args:
        name_of_thing (string): Name of the things to ask for

    Returns:
        list: A list of string inputs from the user
    """

    result_list = []

    item = input("Enter %s: " % name_of_thing)

    while item != "":
        result_list.append(item)
        item = input("Enter another %s: " % name_of_thing)

    return result_list

def get_option(allowed_options):
    """Gets a single item from the user that is one of the given options.

    Args:
        allowed_options (iterable): Any iterable of allowed input strings.

    Returns:
        string: The input that the user picks.
    """

    choice = input("Enter a choice: ")

    while choice not in allowed_options:
        choice = input("Invalid. Try again? ")

    assert choice in allowed_options
    return choice

