import numpy
a= numpy.matrix('1 2; 3 4')
print("Original matrix is:")
print(a)
d=numpy.linalg.det(a)
print("Determinant of a matrix is:")
print(d)
