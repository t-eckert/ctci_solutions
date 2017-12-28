'''
4.1 Implement a function to check if a tree is balanced. For the purposes of 
    this question, a balanced tree is defined to be a tree such that no two 
    leaf nodes differ in distance from the root by more than one.
'''

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.depth = -1 # -1 is not checked.

# Create some trees for testing:

# oak is balanced
oak = Tree()
oak.left = Tree()
oak.left.left = Tree()
oak.left.right = Tree()
oak.right = Tree()
oak.right.left = Tree()
oak.right.right = Tree()

# beech is NOT balanced
beech = Tree()
beech.left = Tree()
beech.left.left = Tree()

def is_balanced(tree, depth):
    # Recursive checker
    # Handle the null case.
    if tree is None:
        return True, 0
    l_balanced, l_depth = is_balanced(tree.left, depth)
    r_balanced, r_depth = is_balanced(tree.right, depth)
    tree.depth = 1 +max(l_depth, r_depth)
    balanced = l_balanced and r_balanced and is_depth_balanced(tree.left, tree.right)
    return balanced, tree.depth

def is_depth_balanced(l_node,r_node):
    if (abs(depth(l_node) -depth(r_node)) <= 1):
        return True
    return False

def depth(tree):
    if tree is None:
        return 0
    else:
        if tree.depth != -1:
            return tree.depth
        else:
            tree.depth = 1 + max(depth(tree.left), depth(tree.right))
            return tree.depth

def main():
    print("Oak is balanced: %s" % is_balanced(oak, 0)[0])
    print("Beech is balanced: %s" % is_balanced(beech, 0)[0])
    pass

main()