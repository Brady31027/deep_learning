import numpy as np

print "----- np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]]) -----"
mat = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])
print mat
"""
Output:
[[1 2 3 4 5]
 [5 6 7 8 9]]
"""

print "\n----- np.zeros((4, 5)) -----"

mat = np.zeros((4, 5))
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value 0.0F.
Default data type us float64
"""

print "\n----- np.zeros((4, 5), dtype=np.float32) -----"

mat = np.zeros((4, 5), dtype=np.float32)
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value 0.0F.
Default data type us float32
"""

print "\n----- np.zeros((4, 5), dtype=np.int) -----"

mat = np.zeros((4, 5), dtype=np.int)
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value 0.
Data type us int64
"""

print "\n----- np.zeros((4, 5), dtype=np.int32) -----"

mat = np.zeros((4, 5), dtype=np.int32)
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value 0.
Data type us int32
"""

print "\n----- np.ones((5, 4)) -----"

mat = np.ones((5, 4))
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value 1.0F.
Default data type us float64
"""

print "\n----- np.empty((5, 4)) -----"

mat = np.empty((5, 4))
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[  1.72723371e-077   1.72723371e-077   1.00000000e+000   2.78134232e-309]
 [  0.00000000e+000   2.24788332e-314   6.92732850e-310   2.12199579e-314]
 [  6.92732850e-310   6.92732850e-310   0.00000000e+000   2.24788373e-314]
 [  6.35862486e-321   9.73469813e-309   0.00000000e+000   2.24790285e-314]
 [  1.00000000e+000   3.95252517e-323   1.49457066e-154   1.39500074e-308]], dtype=float64

Explanation:
Create dimension (4 x 5) matrix with init value ~0.0F.
Default data type us float64
"""

print "\n----- np.arange(10) -----"

mat = np.arange(10)
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[0 1 2 3 4 5 6 7 8 9], dtype=int64

Explanation:
Usage is similar to Python range()/ xrange()
"""

print "\n----- np.arange(10).reshape((2, 5)) -----"

mat = np.arange(10).reshape((2, 5))
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[0 1 2 3 4]
 [5 6 7 8 9]], dtype=int64

Explanation:
Usage is similar to Python range()/ xrange().
Use reshape to reshape the matrix from (1 X 10) to (2 X 5).
Param for reshape() is a tuple (row, col) to represent the dimension.
"""

print "\n----- np.linspace(10, 100, 10) -----"

mat = np.linspace(10, 100, 10)
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[  10.   20.   30.   40.   50.   60.   70.   80.   90.  100.], dtype=float64

Explanation:
Averagly separate range(10, 100) (inclusively) to 10 segments
"""

print "\n----- np.linspace(10, 100, 10).reshape((2, 5)) -----"

mat = np.linspace(10, 100, 10).reshape((2, 5))
print "{mat}, dtype={dtype}".format(mat=mat, dtype=mat.dtype)
"""
Output:
[[  10.   20.   30.   40.   50.]
 [  60.   70.   80.   90.  100.]], dtype=float64

Explanation:
Averagly separate range(10, 100) (inclusively) to 10 segments.
Then reshapre the returned (1 X 10) matrix to (2 X 5).
"""
