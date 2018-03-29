import numpy as np

mat = np.arange(12).reshape((3, 4))
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

matVSplit = np.vsplit(mat, 3)
print matVSplit

"""
Output:
  [ array([[0, 1, 2, 3]]), 
    array([[4, 5, 6, 7]]), 
    array([[ 8,  9, 10, 11]])]
Attention:
  If len(mat) % #partition != 0, error will raise
  E.g. np.vsplit(mat, 2) will cause the following error:
       ValueError: array split does not result in an equal division
"""

matHSplit = np.hsplit(mat, 4)
print matHSplit
"""
Output:
 [ array([[0],
          [4],
          [8]]), 
   array([[1],
          [5],
          [9]]), 
   array([[ 2],
          [ 6],
          [10]]), 
   array([[ 3],
          [ 7],
          [11]])]
"""

matSplitWithAxis0 = np.split(mat, 3, axis=0)
print matSplitWithAxis0
"""
Output:
  [ array([[0, 1,  2,  3]]), 
    array([[4, 5,  6,  7]]), 
    array([[8, 9, 10, 11]])]

Explanation:
  Same as vsplit(mat, 3)
"""

matSplitWithAxis1 = np.split(mat, 2, axis=1)
print matSplitWithAxis1
"""
Output:
 [ array([[0, 1],
          [4, 5],
          [8, 9]]), 
   array([[ 2,  3],
          [ 6,  7],
          [10, 11]])]

Explanation:
  Same as hsplit(mat, 2)
"""

matArraySplitWithAxis0 = np.array_split(mat, 2, axis=0)
print matArraySplitWithAxis0
"""
Output:
 [ array([[0, 1, 2, 3],
         [4, 5, 6, 7]]), 
   array([[ 8,  9, 10, 11]])]

Explanation:
  As we mentioned, if len(mat) % #partition != 0, error will raise.
  However, if we use array_split, we can fix this error by trancate the tailing array partition
"""