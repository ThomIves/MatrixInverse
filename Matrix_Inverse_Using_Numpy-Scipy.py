import numpy as np
from numpy.linalg import inv


a = np.array([[5., 3., 1.], [3., 9., 4.], [1., 3., 5.]])
print(a, '\n')

ainv = inv(a)
ainv = ainv.round(3)

print(ainv)
