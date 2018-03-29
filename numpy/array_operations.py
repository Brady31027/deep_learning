import numpy as np

mat1 = np.array([6, 6, 6])
mat2 = np.array([2, 2, 2])
matAdd = mat1 + mat2
matSub = mat1 - mat2
matMul = mat1 * mat2
matDiv = mat1 / mat2
print "add={}, sub={}, mul={}, div={}".format(matAdd, matSub, matMul, matDiv)
"""
Output:
add=[8 8 8], sub=[4 4 4], mul=[12 12 12], div=[3 3 3]
"""

mat1Square = mat1 ** 2
print mat1Square
"""
Output: [36 36 36]
"""

matTriFunc = np.sin( np.array([3.14/2, 3.14/2, 3.14/2]))
print matTriFunc
"""
Output: [ 0.99999968  0.99999968  0.99999968]
Explanation: map function to every matrix element
Similar to traditional Python: matOut = map(lambda x: Math.sin(x), matIn_1D)
"""

matBooleanIn = np.array([1, 2, 3])
matBooleanOut = (matBooleanIn != 2)
print matBooleanOut
"""
Output: [ True False  True]
Explanation: map condition to every element in matrix
"""

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
matDot = np.dot(mat1, mat2)
print matDot
"""
Output:
 [[19 22]
  [43 50]]
"""

mat = np.random.random((2, 4))
print mat
print "sum = {}".format( np.sum(mat) )
print "max = {}".format( np.max(mat) )
print "min = {}".format( np.min(mat) )
"""
Output:
  [[ 0.30624584  0.2800242   0.06201043  0.04772351]
   [ 0.93830754  0.69754147  0.75802908  0.44580564]]
  sum = 3.53568770218
  max = 0.938307542586
  min = 0.0477235125739

Explanation: Generate 2 X 4 random numbers which are in range [0, 1]  
"""

mat = np.random.random((2, 4))
print mat
print "sum for axis 0 = {}".format( np.sum(mat, axis=0) )
print "max for axis 1 = {}".format( np.max(mat, axis=1) )
print "min for axis 0 = {}".format( np.min(mat, axis=0) )
"""
Output:
  [[ 0.25411015  0.22303828  0.10115059  0.8504017 ]
   [ 0.8989571   0.90370716  0.43498943  0.18313321]]
  sum for axis 0 = [ 1.15306725  1.12674544  0.53614002  1.03353491]
  max for axis 1 = [ 0.8504017   0.90370716]
  min for axis 0 = [ 0.25411015  0.22303828  0.10115059  0.18313321]
"""

