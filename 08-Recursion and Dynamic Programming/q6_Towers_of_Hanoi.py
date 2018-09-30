"""
8.6 Towers of Hanoi: In the classic problem in the Towers of Hanoi, you have 
    3 towers and N disks of different sizes which can slide onto any tower. 
    The puzzle starts with disks sorted in ascending order of size from top to
    bottom. You have the following contraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto another tower.
    (3) A disk cannot be placed on top of a smaller disk.
    Write program to move the disks from the first tower to the last using 
    stacks.
"""

from timeit import default_timer as timer
import matplotlib.pyplot as plt

# Let's define the stacks that represent the three towers (A, B, and C)
# The A stack will be created in a function so that we can change its
# length at runtime. The size of each disk is represented by an integer.


def create_tower_A(height):
    return [i for i in range(height, 0, -1)]


B, C = [], []

# This problem is solved using a simple recursive operation.
# I have included a parameter print_out that will display the values in each
# tower if 1 and won't if 0.
def solve(n, from_tower, temp_tower, to_tower, print_out):
    """ Recursive operation to solve Tower of Hanoi problem.
        n is height of first tower (A)
        each tower is stack
        print_out == 1 -> print the towers; 0 -> don't
    """
    if n > 0:
        # Move tower of size n-1 to the temp_tower
        solve(n - 1, from_tower, to_tower, temp_tower, print_out)
        # Move disk from the from_tower to to_tower
        if from_tower:
            move_disk(from_tower, to_tower, print_out)
        # Move tower of size n-1 from temp_tower to to_tower
        solve(n - 1, temp_tower, from_tower, to_tower, print_out)


def move_disk(from_tower, to_tower, print_out):
    """ Move the disk in memory to a different tower as specified.
        print_out == 1 -> print the towers; 0 -> don't
    """
    to_tower.append(from_tower.pop())
    if print_out == 1:
        print("A: %s\nB: %s\nC: %s\n" % (A, B, C))


# First let's run the puzzle for a user defined height.
A = create_tower_A(int(input("Towers of Hanoi puzzle with height: ")))
print("A: %s\nB: %s\nC: %s\n" % (A, B, C))
solve(len(A), A, B, C, 1)

# Now, let's test how the length of time to solve the puzzle increases
# with the height of the initial puzzle.
x = []
y = []

for i in range(1, 30):
    start = timer()
    A = create_tower_A(i)
    solve(len(A), A, B, C, 0)
    end = timer()
    print("Towers of Hanoi with height %s. Time: %s" % (i, end - start))
    x.append(i)
    y.append(end - start)

# The increase should be exponential: O(e^N)
plt.plot(x, y)
plt.xlabel("Initial height of tower A")
plt.ylabel("Time to solve puzzle (s)")
plt.show()
