import numpy as np

mat = np.arange(12).reshape((3, 4))
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

print mat[1]
"""
Output [4, 5, 6, 7]
"""

print mat[1][2]
"""
Output 6
"""

print mat[1, 2]
"""
Output 6
"""

print mat[1, 1:3]
"""
Output [5, 6]
"""

for row in mat:
	print row
"""
Output:

[0 1 2 3]
[4 5 6 7]
[8 9 10 11]
"""

for col in mat.T:
	print col
"""
Output:

[0 4 8]
[1 5 9]
[2  6 10]
[3  7 11]

Explanation:
Transpose: rotate 90 degree clock-wise
"""

flatMat = mat.flatten()
print flatMat
"""
Output: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Explanation: Flatten a multi-dimension matrix to (1 X N) matrix
"""

for item in mat.flat:
	print item
"""
Output:
0
1
2
3
4
5
6
7
8
9
10
11
"""
