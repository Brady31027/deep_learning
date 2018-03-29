import numpy as np

mat = np.array([  [1,   2,  3],
                  [4,   5,  6],
                  [7,   8,  9],
                  [10, 11, 12]
	])

print mat
"""
Output:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""

print mat.shape
"""
Output: (4, 3)
Explanation: 4 rows, 3 cols
"""

print mat.ndim
"""
Output: 2
Explanation: 2 dimensions (x & y)
"""

print mat.size
"""
Output: 12
Explanation: total 12 elements
"""
