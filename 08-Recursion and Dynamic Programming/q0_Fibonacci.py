"""
8.1 Write a method to generate the nth Fibonacci number.
"""

from timeit import default_timer as timer


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
    1, 1, 2, 3, 5, 8, 13, 21
"""


def main():
    for i in range(1, 50):
        start = timer()
        num = fibonacci(i)
        end = timer()
        print("%s \t %s \t %s" % (i, num, (end - start) * 10 ** 7))


main()
