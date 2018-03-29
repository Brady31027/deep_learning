import numpy as np

mat1 = np.arange(10, 20)
mat2 = np.arange(20, 30)
verticalMergeMat = np.vstack((mat1, mat2))
print verticalMergeMat
print "mat1 shape={mat1}, mat2 shape={mat2}, hmat shape={vmat}".format( \
	mat1=mat1.shape, \
	mat2=mat2.shape, \
	vmat=verticalMergeMat.shape )
"""
Output:
     [[10 11 12 13 14 15 16 17 18 19]
      [20 21 22 23 24 25 26 27 28 29]]
     mat1 shape=(10,), mat2 shape=(10,), hmat shape=(2, 10) 

Attention: shape (10,) doesn't mean it has 10 rows, it means it has one row and 10 col instead.

Explanation:
Vertically merge two matrix.
If lenth of two matrix are not match, we will get the following error:
  * ValueError: all the input array dimensions except for the concatenation axis must match exactly
If the input matrix is multi-row, e.g

mat1 = np.arange(10, 20).reshape((2,5))
mat2 = np.arange(20, 30).reshape((2,5))
np.vstack((mat1, mat2)) will do the following
  (1). vstack mat1 and mat2 separately
  (2). vstack the processed mat1 and mat2
  (3). Turn out to be like:
       
       [[10 11 12 13 14]
        [15 16 17 18 19]
        [20 21 22 23 24]
        [25 26 27 28 29]]
"""

horizontalMergeMat = np.hstack((mat1, mat2))
print horizontalMergeMat
print "mat1 shape={mat1}, mat2 shape={mat2}, hmat shape={hmat}".format( \
	mat1=mat1.shape, \
	mat2=mat2.shape, \
	hmat=horizontalMergeMat.shape )
"""
Output: [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]
        mat1 shape=(10,), mat2 shape=(10,), hmat shape=(20,)

Attention: shape (10,) doesn't mean it has 10 rows, it means it has one row and 10 col instead.

Explanation:
Concate these two input matrix
But if we mis-treat them as Python built-in lists and type mat1 + mat2,
we will get [30 32 34 36 38 40 42 44 46 48]
"""


array2D = np.array([[1, 2, 3], [4, 5, 6]])
print "{} with shape {}".format(array2D, array2D.shape)
print "{} with shape {}".format(array2D.T, array2D.T.shape)
array1D = np.array([1, 2, 3])
print "{} with shape {}".format(array1D, array1D.shape)
print "{} with shape {}".format(array1D.T, array1D.T.shape)
"""
Output:
  [[1 2 3]
   [4 5 6]] with shape (2, 3)
  [[1 4]
   [2 5]
   [3 6]] with shape (3, 2)
  [1 2 3] with shape (3,)
  [1 2 3] with shape (3,) 

Attention:
(1). np.array([1, 2, 3]) -> shape is (3,) -> we CANNOT transpose it
(2). np.array([[1, 2, 3]]) -> shape is (1, 3) -> we can transpose it
  
Question:
According to this example, how can we change matrix with shape (3,) to matrix with shape (1, 3)?
"""

array1D = np.array([1, 2, 3])
array1DNewRowAxis = array1D[np.newaxis, : ]
array1DNewColAxis = array1D[:, np.newaxis]
print "Add new axis to row of array1D {} with shape {}".format(array1DNewRowAxis, array1DNewRowAxis.shape)
print "Transpose array to {} with shape {}".format(array1DNewRowAxis.T, array1DNewRowAxis.T.shape)
print "Add new axis to col of array1D {} with shape {}".format(array1DNewColAxis, array1DNewColAxis.shape)
"""
Output:
  Add new axis to row of array1D [[1 2 3]] with shape (1, 3)
  Transpose array to [[1]
                      [2]
                      [3]] with shape (3, 1)
  Add new axis to col of array1D [[1]
                                  [2]
                                  [3]] with shape (3, 1)
"""


array1D1 = np.array([1, 1, 1])[ : , np.newaxis]
array1D2 = np.array([2, 2, 2])[ : , np.newaxis]
array1D3 = np.array([3, 3, 3])[ : , np.newaxis]
hArray = np.hstack((array1D1, array1D2, array1D3))
cArray = np.concatenate((array1D1, array1D2, array1D3), axis=1)
print "using hstack"
print hArray
print "using concatenate"
print cArray
"""
Output:
  using hstack
   [[1 2 3]
    [1 2 3]
    [1 2 3]]
  using concatenate
   [[1 2 3] 
    [1 2 3]
    [1 2 3]]

Explanation:
concatenate() brings axis as one of its parameters.
where
  axis = 0: vertical
  axis = 1: horizontal
"""
