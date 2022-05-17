import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import csr_matrix

row_A = np.array([0, 0, 1, 2 ])
col_A = np.array([0, 1, 0, 1])
data_A = np.array([4, 7, 8, 1])

cscMatrix = csc_matrix((data_A, (row_A, col_A)),shape = (3, 3))


print("csc matrix: \n", cscMatrix.toarray())


row_B = np.array([0, 1, 1, 2 ])
col_B = np.array([0, 0, 1, 0])
data_B = np.array([5, 2, 9, 1])

csrMatrix_B = csr_matrix((data_B, (row_B, col_B)),shape = (3, 3))


print("csr matrix:\n", csrMatrix_B.toarray())

sparseMatrix = cscMatrix.multiply(csrMatrix_B)

print("Product csc with csr Matrix:\n",
	sparseMatrix.toarray() )


sparseMatrix = csrMatrix_B.multiply(cscMatrix)

print("Product csr with csc Matrix:\n", sparseMatrix.toarray() )
