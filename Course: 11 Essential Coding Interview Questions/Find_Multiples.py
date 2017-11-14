'''
Find two integers in an array that multiply to a given value.
Find three integers in an array that multiply to a given value.
'''

from timeit import default_timer as timer

input_lists = [
    [2,1,5,40],
    [2,3,10],
    [1,1,2,3,5,8,13],
    [6,3,4,2,5,1,6,7,8,3,4,5,8,10,2,3,4,1,5,2,6,7,7,4,2,2,1,4,3,5,2,67]
]


def two_multiples(input_list, product):
    ''' Finds if two integers in the list multiply to the product: T/F'''
    # The minimum time possible requires that we at least look at enough values
    # in the input_list to determine whether to return True or False.
    # For the True case, this means only looking at enough values to find two
    # that satisfy the case. 
    # For the False case, this means looking at every value in input_list.
    multiples = []
    for i in range(len(input_list)):
        # We only care about integer solutions
        if product % input_list[i] == 0:
            if product / input_list[i] in multiples:
                return True
            else: 
                multiples.append(input_list[i])
    return False

def three_multiples(input_list, product):
    '''Finds if three integers in the list multiply to the product: T/F'''
    # We can simply extend our function from above. If the remainder is an int
    # push it into two_multiples with the list.
    for i in range(len(input_list)):
        if product % input_list[i] == 0:
            validity = two_multiples(
                input_list[:i]+input_list[i+1:], 
                product/input_list[i])
            if validity == True:
                return True
    return False

start_all = timer()
for product in range(1,100):
    for i in range(len(input_lists)):
        start_two = timer()
        print('Two factors of %s in %s : %s' % (product, input_lists[i], two_multiples(
            input_lists[i], product)))
        end_two = timer()
        print("Process Time: %s s" % (end_two-start_two))
        start_three = timer()
        print('Three factors of %s in %s : %s' % (product, input_lists[i], three_multiples(
            input_lists[i], product)))
        end_three = timer()
        print("Process Time: %s s" % (end_three - start_three))
end_all = timer()
print("Total time: %s s" % (end_all-start_all))