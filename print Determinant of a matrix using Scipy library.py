import numpy
from scipy import linalg
a= numpy.matrix('1 2; 3 4')
print("Original matrix is:")
print(a)
d=linalg.det(a)
print("Determinant of a matrix is:")
print(d)
