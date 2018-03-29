import numpy as np

mat = np.array([[5, 8, 1], [2, 9, 7]])
"""
[[5 8 1]
 [2 9 7]]
"""

minValue = np.min(mat)
maxValue = np.max(mat)
minValueIndex = np.argmin(mat)
maxValueIndex = np.argmax(mat)

print "mat[{}] has min value {}, mat[{}] has max value {}".format(minValueIndex, \
	                                                              minValue, \
	                                                              maxValueIndex, \
	                                                              maxValue)
"""
mat[2] has min value 1, mat[4] has max value 9
"""

meanValue = np.mean(mat)
averageValue = np.average(mat)
medianValue = np.median(mat)

print "mean: {}, average: {}, median: {}".format(meanValue, averageValue, medianValue)
"""
mean: 5.33333333333, average: 5.33333333333, median: 6.0
"""

cumSumArray = np.cumsum(mat)
print "cumSum = {}".format(cumSumArray)
"""
Output: cumSum = [ 5 13 14 16 25 32]
Explanation:
  5  = mat[0][0] 
  13 = mat[0][0] + mat[0][1]
  14 = mat[0][0] + mat[0][1] + mat[0][2]
  16 = mat[0][0] + mat[0][1] + mat[0][2] + mat[1][0]
  25 = mat[0][0] + mat[0][1] + mat[0][2] + mat[1][0] + mat[1][1]
  32 = mat[0][0] + mat[0][1] + mat[0][2] + mat[1][0] + mat[1][1] + mat[1][2]
"""

diffArray = np.diff(mat)
print "diff = {}".format(diffArray)
"""
Output:
  diff = [[ 3 -7]
          [ 7 -2]]

Explanation:
  Recall mat = [[5 8 1]
                [2 9 7]]
  diffArray[0][0] = mat[0][1] - mat[0][0]
  diffArray[0][1] = mat[0][2] - mat[0][1]
  diffArray[1][0] = mat[1][1] - mat[1][0]
  diffArray[1][1] = mat[1][2] - mat[1][1]
"""

matContainZero = np.array([ [1, 0, 2, 0, 3, 0],
                            [0, 4, 0, 5, 0, 6],
                            [7, 8, 9, 0, 0, 0],
                            [0, 0, 0, 10, 11, 12]
	                      ])
matNonZero = np.nonzero(matContainZero)
print matNonZero
"""
Output:
  (array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]), 
   array([0, 2, 4, 1, 3, 5, 0, 1, 2, 3, 4, 5]))

Explanation:
   First array indicates the row number, represented as "i"
   Second array contains indices that matContainZero[index] != 0, represented as "j"
   Then, matNonZero[0][0] == 1 != 0
         matNonZero[0][2] == 2 != 0
         matNonZero[0][4] == 3 != 0
         matNonZero[1][1] == 4 != 0
         ...etc
"""

sortedMat = np.sort(mat)
print sortedMat
"""
Output:
  [[1 5 8]
   [2 7 9]]

Explanation:
  Recall mat = [[5 8 1]
                [2 9 7]]
  np.sort() will sort the matrix in descending order per row
"""

transposedMat1 = np.transpose(mat)
transposedMat2 = mat.T
print transposedMat1
print transposedMat2
"""
Output:
 [[5 2]
  [8 9]
  [1 7]]
 [[5 2]
  [8 9]
  [1 7]]
"""

matForClip = np.arange(16).reshape(4, 4)
clippedMat = np.clip(matForClip, 5, 10)
print clippedMat
"""
Output:
  [[ 5  5  5  5]
   [ 5  5  6  7]
   [ 8  9 10 10]
   [10 10 10 10]]

Explanation:
  For each element that less than 5, clip to 5.
  For each element that greater than 10, clip to 10.
"""