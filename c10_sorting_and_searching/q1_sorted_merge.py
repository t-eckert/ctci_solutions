"""
  10.1 You are given two sorted arrays, A and B. A has a large enough buffer 
    to hold B. Write a method to merge B into A in a sorted order. 
"""

"""
  While Python offers a built-in function to handle this,
    sorted(A+B)
  let's write this ourselves. 
"""


def merge_sorted_lists(A, B):
    buffer_index = A.index(None)
    input_index = len(B)
    buffer_size = len(A) - buffer_index

    if buffer_size < len(B):
        print("Buffer too small!")
        return None

    for insertion_index in range(buffer_index + input_index, 1, -1):
        print(
            "At index {insertion_index} comparing A[{input_index - 1}]={B[input_index - 1} and B[{buffer_index - 1}]={A[buffer_index - 1]}"
        )
        if B[input_index - 1] >= A[buffer_index - 1]:
            A[insertion_index - 1] = B[input_index - 1]
            A[insertion_index - 2] = A[buffer_index - 1]
            input_index -= 1
        else:
            A[insertion_index - 1] = A[buffer_index - 1]
            A[insertion_index - 2] = B[input_index - 1]
            buffer_index -= 1
        print(A)
    return A

