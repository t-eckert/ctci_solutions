"""
  16.1 Number Swapper: Write a function to swap a number in place.
"""

test_numberPairs = [
    (2, 3),
    (1, 1),
    (362943.273415, 15115234283.9958300288593),
    (-3.14159, 3.14159),
]


def swap_in_place(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b


def main():
    for test_numberPair in test_numberPairs:
        a, b = test_numberPair
        print("%s, %s" % (a, b))
        a, b = swap_in_place(a, b)
        print("swapped in place -> %s, %s" % (a, b))


main()
