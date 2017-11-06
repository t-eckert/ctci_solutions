'''
1.4 Palindrome Permutation: Given as string, write a function to check if it is
    a permutation of a palindrome. The palindrome does not need to be limited
    to just dictionary words. 

    EXAMPLE:
    input = Tact Coa
    output = True 
    There exist permutation of the string 'tactcoa' that are palidromes (i.e. 'tacocat')
'''

from timeit import default_timer as timer

# Let's begin by thinking of what qualifies a list of values as a palindrome.
# Each value must have a pair exempting one if the length of the list is odd.

inputs = {
    0 : 'Tact Coa',
    1 : 'Rainbow'
} 

def check_palindrome_permute(str_input):
    '''Checks if a given string or list is a permutation of a palindrome'''
    # To have a robust function that can handle spaces and capitalization,
    # let's strip whitespace from the input and set all letters to 
    # lower case. I'm going to include punctuation as possible values 
    # used in the palindrome.
    str_input = ''.join(str_input.split()).lower() 
    # Create a set of all unique values in the input
    values_in_input = list(set(str_input))
    if len(str_input) % 2 == 0:
        # If the string has an even number of chars, each needs at least a pair
        for i in range(len(values_in_input)):
            if str_input.count(values_in_input[i]) % 2 != 0:
                return False
    else:
        # If the string has an odd number of chars, there can be one value
        # that doesn't have a pair
        single = 0
        for i in range(len(values_in_input)):
            if single > 1:
                return False
            if str_input.count(values_in_input[i]) % 2 != 0:
                single += 1
    return True

start = timer()
for i in range(len(inputs)):
    print("%s is a perumation of a palindrome: %s" % (inputs[i], check_palindrome_permute(inputs[i])))
end = timer()
print("Tested %s values in %.2f ns." % (len(inputs), (end-start)*10**9))