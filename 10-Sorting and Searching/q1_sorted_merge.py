'''
  10.1 You are given two sorted arrays, A and B. A has a large enough buffer 
    to hold B. Write a method to merge B into A in a sorted order. 
'''

'''
  While Python offers a built-in function to handle this,
    sorted(A+B)
  let's write this ourselves. 
'''

test_lists = [
  ([2, 3, 5, None, None, None, None],
   [1, 4, 9]),
  ([45, 904, 1023, 9000, None, None, None],
   [3, 1015, 8977])
]

def merge_sorted_lists(A, B):
  A_i = A.index(None)
  B_i = len(B)
  for m_i in range(A_i+B_i,1,-1):
    print("At index %s comparing A[%s]=%s and B[%s]=%s" % (m_i,B_i-1,B[B_i-1],A_i-1,A[A_i-1]))
    if B[B_i-1] >= A[A_i-1]:
      A[m_i-1] = B[B_i-1]
      A[m_i-2] = A[A_i-1]
      B_i -= 1
    else:
      A[m_i-1] = A[A_i-1]
      A[m_i-2] = B[B_i-1]
      A_i -= 1
    print(A)
  return A

def main():
  for tests in test_lists:
    A, B = tests
    print(merge_sorted_lists(A,B))

main()
  