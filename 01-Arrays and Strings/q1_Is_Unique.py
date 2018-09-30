"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
    characters. What if you cannot use additional data structures?
"""

"""
Because Python doesn't require a type definition for the input of a function,
we can be clever and write a function that will determine the "uniqueness" of 
a string or a list depending on what is input. 
"""


def are_items_unique(str_or_list):
    """True if no repeated values in string or list. False otherwise."""
    # Let's try and only traverse the input once to save time.
    # As we traverse the input, we can check if the value is in a list
    # called read_values. If it isn't, we add it to read_values.
    # If it is, we return False and break before reading through
    # the entirety of the input because we have enough information
    # to determine uniqueness.
    read_values = []
    for item in str_or_list:
        if item in read_values:
            return False
        else:
            read_values.append(item)
    return True


def are_items_unique_single_datastructure(str_or_list):
    """True if no repeated values in string or list. False otherwise.
  Uses no additional data structures."""
    # If we're going to write check_unique without any additional data
    # structures we can use the count() method in Python. We iterate
    # through the values in the input and check the number of occurances
    # of that value in the array.
    for i in range(len(str_or_list)):
        if str_or_list.count(str_or_list[i]) != 1:
            return False
    return True
