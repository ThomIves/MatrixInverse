<<<<<<< HEAD
import numpy as np
from numpy.linalg import inv


a = np.array([[5., 3., 1.], [3., 9., 4.], [1., 3., 5.]])
print(a, '\n')

ainv = inv(a)
ainv = ainv.round(3)

print(ainv)
=======
import numpy as np
from numpy.linalg import inv


a = np.array([[5., 3., 1.], [3., 9., 4.], [1., 3., 5.]])
print(a, '\n')

ainv = inv(a)
ainv = ainv.round(3)

print(ainv)
>>>>>>> 7b6dac91eaad3501f2ee5e18c151c6f6b5c913e6
