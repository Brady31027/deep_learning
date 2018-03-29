import numpy as np

mat = np.arange(10)
"""
[0 1 2 3 4 5 6 7 8 9]
"""
matShallowCopy = mat
print matShallowCopy
mat[0] = 9
print matShallowCopy

mat = np.arange(10)
matDeepCopy = mat.copy()
print matDeepCopy
mat[0] = 9
print matDeepCopy

"""
Output:
[0 1 2 3 4 5 6 7 8 9] # shallow copy
[9 1 2 3 4 5 6 7 8 9] # value changed because mat is changed
[0 1 2 3 4 5 6 7 8 9] # deep copy
[0 1 2 3 4 5 6 7 8 9] # value doesn't change regardless that mat is changed
"""
