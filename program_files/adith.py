import numpy as np
from numpy.lib import matrix
one_D=np.array([1,2,3,4])
print(one_D)

#2-D ARRAY 
two_D = np.array([[1,2,3],[4,5,6]])
print(two_D)
print(two_D.ndim)
print(two_D.shape)
print(two_D.itemsize)

#3-D ARRAY 
three_D=np.array([
                   [1,2,3],[3,4,5]
                   [6,7,8],[10,11,12]
               ])
print(three_D)

one_D=np.arange(1,25)
two_D = one_D.reshape(6,4)
one_D=np.ravel(two_D)


two_D=np.arange(1,36).reshape(6,6)
sub=two_D[1:4,3:6]

