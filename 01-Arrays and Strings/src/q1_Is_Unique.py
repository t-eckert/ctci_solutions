'''
1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
    characters. What if you cannot use additional data structures?
'''

'''
Because Python doesn't require a type definition for the input of a function,
we can be clever and write a function that will determine the "uniqueness" of 
a string or a list depending on what is input. 
'''

from timeit import default_timer as timer

# We create a few inputs to test the function. I chose to use a dictionary
# to store the inputs because it offers more visual clarity than nesting 
# lists in lists. The computer shouldn't really notice a difference 
# performance-wise.
inputs = {
    0 : 'Bananagram',
    1 : 'String',
    2 : 'Strings',
    3 : [3,1,4],
    4 : [1,1,2,3,5,8]
}

def are_items_unique(str_or_list):
    '''True if no repeated values in string or list. False otherwise.'''
    # Let's try and only traverse the input once to save time. 
    # As we traverse the input, we can check if the value is in a list
    # called read_values. If it isn't, we add it to read_values.
    # If it is, we return False and break before reading through 
    # the entirety of the input because we have enough information
    # to determine uniqueness.
    read_values = []
    for i in range(len(str_or_list)):
        if str_or_list[i] in read_values:
            return False
        else:
            read_values.append(str_or_list[i])
    return True

def check_unique_wo_ds(str_or_list):
    '''True if no repeated values in string or list. False otherwise.
       Uses no additional data structures.'''
    # If we're going to write check_unique without any additional data
    # structures we can use the count() method in Python. We iterate
    # through the values in the input and check the number of occurances
    # of that value in the array.
    for i in range(len(str_or_list)):
        if str_or_list.count(str_or_list[i]) != 1:
            return False
    return True

print("Using 'check_unique()'")
start_w_ds = timer()
for i in range(len(inputs)):
    print("%s is unique: %s" % (inputs[i], check_unique(inputs[i])))
end_w_ds = timer()
print('Runtime with data structures for %s values = %.2f ns' % (len(inputs),(end_w_ds-start_w_ds)*10**9))

print("\nUsing 'check_unique_wo_ds()'")
start_wo_ds = timer()
for i in range(len(inputs)):
    print("%s is unique: %s" % (inputs[i], check_unique_wo_ds(inputs[i])))
end_wo_ds = timer()
print('Runtime with data structures for %s values = %.2f ns' % (len(inputs),(end_wo_ds-start_wo_ds)*10**9))

user_check = input('\nCheck your own string or list: ')
print("%s is unique: %s" % (user_check, check_unique(user_check)))