"""
3.3 Stack of Plates: Imagine a stack of plates. If the stack gets too high, it
    might topple. Therefore, in real life, we would likely start a new stack
    when the previous stack exceeds some threshold. Implement a data structure 
    SetOfStacks that mimics this. SetOfStacks should be composed of several 
    stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a 
    single stack.
"""


class SetOfStacks:

    # We will need the __init__ function to create the structure.
    # It will take a reference to the structure, self, and to the max height
    # of each stack, threshold.
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def push(self, item):
        # Check if the stack is full and create a new stack if it is.
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.threshold:
            self.stacks.append([])
        # Add the value to the last part in the stack.
        self.stacks[-1].append(item)

    def pop(self):
        # Check if the set of stacks is empty. If so, return a message that it is.
        if len(self.stacks) == 0:
            return "Set of stacks is empty."
        item = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return item


def test_SetOfStacks():
    threshold = int(input("Set the maximum height for the stack: "))
    set_of_stacks = SetOfStacks(threshold)

    print("Let's fill up 3 stacks.")
    for i in range(threshold * 3):
        set_of_stacks.push(input("Push: "))

    print("Now let's pop the third stack!")
    for i in range(threshold):
        print("Pop: %s" % set_of_stacks.pop())


test_SetOfStacks()
