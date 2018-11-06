# Linear Regression - Library Free, i.e. no numpy or scipy 


def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")

def check_non_singular(A):
    """
    Checks that matrix is not singular by checking 
    for a non-singular determinant.
        :param A: The matrix to check

        :return: The determinant 
                (any non-zero determinant will serve as a True)
    """
    AC = copy_matrix(A)
    for row in range(len(AC)):
        AC[row] = AC[row] + AC[row][:-1]
    
    down = 0
    up = 0
    for diag in range(len(A[0])):
        this_down = 1.0
        for element in range(len(A[0])):
            this_down *= AC[element][element + diag]
        down += this_down

        this_up = 1.0
        for element in range(len(A[0])):
            reverse_element = len(A) - 1 - element
            this_up *= AC[reverse_element][element + diag]
        up += this_up

    determinant = down - up

    if determinant != 0:
        return determinant
    else:
        raise ArithmeticError("Singular Matrix!")

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :returns: list of lists that form the matrix.
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix

        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied

        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M):
    """
    docstring here
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x,3)+0 for x in row])

def transpose(M):
    """
    Creates and returns a transpose of a matrix.
        :param M: The matrix to be transposed

        :return: the transpose of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def matrix_multiply(A,B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix

        :return: The product of the two matrices
    """
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def check_matrix_equality(A,B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check

        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],tol) != round(B[i][j],tol):
                    return False

    return True

def inverse_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed

        :return: The inverse of the matrix A
    """
    check_squareness(A)
    check_non_singular(A)

    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Make all diagonal elements 1 and make the lower triangular matrix all 0’s
    for fd in range(n): # fd is for focus diagonal
        for i in range(fd,n):
            if i == fd:
                scaler = 1.0 / AM[i][fd]
            else:
                scaler = AM[i][fd]
            for j in range(n):
                if i == fd:
                    AM[i][j] *= scaler
                    IM[i][j] *= scaler
                else:
                    AM[i][j] = AM[i][j] - scaler * AM[fd][j]
                    IM[i][j] = IM[i][j] - scaler * IM[fd][j]

    # Make the upper triangular matrix all 0’s
    for fd in range(n-1,0,-1):
        for i in range(fd-1,-1,-1):
            scaler = AM[i][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - scaler * AM[fd][j]
                IM[i][j] = IM[i][j] - scaler * IM[fd][j]

    # Make sure that IM is an inverse of A
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")
