"""
5.1 Inset Bits: You are given 32-bit numbers, N and M, and two bit positions,
    i and j. Write a method to set all bits between i and j in N equal to M.

    Example: 
    Input = {
        N = 1000000000000,
        M = 10101,
        i = 2,
        j = 6
    }
    Output = { N = 1000001010100 }
"""


class Error(Exception):
    """Base class for exceptions."""

    pass


class BinaryException(Error):
    """Raised when the user inputs non-binary numbers."""

    pass


class SizeException(Error):
    """Raised when M or N are not 32-bit."""

    pass


class BitPositionException(Error):
    """Raised when the difference in bit positions is not the length of M"""

    pass


test_numbers = [
    (1000000000000, 10101, 2, 6),  # pass
    (1000000002000, 10101, 2, 6),  # not pass
    (1000000000000, 10101, 2, 4),  # not pass
    (10000000000000000000000000000000, 10101, 6, 10),  # pass
    (100000000000000000000000000000000, 10101, 6, 10),  # not pass
]


def inset_bits(N, M, i, j):
    """
        Takes in two 32-bit numbers, binary numbers, N and M, and two bit positions, i and j.
        Returns N with bits from i to j set equal to M.
    """
    try:
        # Convert N and M into lists of values
        N_list = [int(i) for i in str(N)]
        M_list = [int(i) for i in str(M)]

        # Check that both inputs are binary numbers
        if not is_binary(N_list):
            raise BinaryException
        if not is_binary(M_list):
            raise BinaryException

        # Check that both inputs are 32-bit
        if not is_32_bit(N_list):
            raise SizeException
        if not is_32_bit(M_list):
            raise SizeException

        # Check that j-i+1 is the length of M_list
        if j - i + 1 is not len(M_list):
            raise BitPositionException

        N_list = N_list[: len(N_list) - j - 1] + M_list + N_list[len(N_list) - i :]
        N = int("".join(str(i) for i in N_list))

        return N

    except BinaryException:
        print("N and M must both be binary.")
    except SizeException:
        print("N and M must be 32 bit integers.")
    except BitPositionException:
        print("j-i+1 must = len(M_list)")


def is_binary(num_list):
    """
        If the input number is not a list of 1's and 0's, return false. Else true.
    """
    for digit in num_list:
        if digit != 1 and digit != 0:
            return False
    return True


def is_32_bit(num_list):
    """
        If the input number is not a 32-bit value, return false. Else true.
    """
    if len(num_list) > 32:
        return False
    return True


def main():
    for test_number in test_numbers:
        N, M, i, j = test_number
        print(inset_bits(N, M, i, j))


main()
