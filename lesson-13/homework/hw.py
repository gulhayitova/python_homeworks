import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
vec = np.arange(10, 50)
print("Vector:", vec)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.
mat3x3 = np.arange(9).reshape(3,3)
print("\n3x3 Matrix:\n", mat3x3)

# 3. Create a 3x3 identity matrix.
eye = np.eye(3)
print("\nIdentity Matrix:\n", eye)

# 4. Create a 3x3x3 array with random values.
arr3D = np.random.rand(3,3,3)
print("\n3D Array:\n", arr3D)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.
bigarr = np.random.rand(10, 10)
minn = bigarr.min()
maxx = bigarr.max()
print("\nMin:", minn, "Max:", maxx)

# 6. Create a random vector of size 30 and find the mean value.
randvec = np.random.rand(30)
mean = randvec.mean()
print("\nMean:", mean)

# 7. Normalize a 5x5 random matrix.
m = np.random.rand(5,5)
m = (m - m.min()) / (m.max() - m.min())
print("\nNormalized Matrix:\n", m)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
m1 = np.random.rand(5,3)
m2 = np.random.rand(3,2)
prod = np.dot(m1, m2)
print("\nProduct of 5x3 and 3x2:\n", prod)

# 9. Create two 3x3 matrices and compute their dot product.
a = np.random.rand(3,3)
b = np.random.rand(3,3)
dot = np.dot(a, b)
print("\nDot Product:\n", dot)

# 10. Given a 4x4 matrix, find its transpose.
m4 = np.random.rand(4,4)
trans = m4.T
print("\nTranspose:\n", trans)

# 11. Create a 3x3 matrix and calculate its determinant.
m3 = np.random.rand(3,3)
det = np.linalg.det(m3)
print("\nDeterminant:", det)

# 12. Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B ).
matA = np.random.rand(3,4)
matB = np.random.rand(4,3)
matprod = np.dot(matA, matB)
print("\nMatrix (3x4) * (4x3):\n", matprod)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
mtrx = np.random.rand(3,3)
vec = np.random.rand(3,1)
m_v_prod = np.dot(mtrx, vec)
print("\nMatrix-Vector Product:\n", m_v_prod)
# 14. Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.
A = np.random.rand(3,3)
b = np.random.rand(3,1)
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:\n", x)
# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
bigmat = np.random.rand(5,5)
rsum = bigmat.sum(axis=1)
csum = bigmat.sum(axis=0)
print("\nRow sums:", rsum)
print("Col sums:", csum)




