# Linear Regression - Library Free, i.e. no numpy or scipy 


def check_squareness(A):
    if len(A) != len(A[0]):
        print("Matrix must be square to inverse.")
        sys.exit()

def zeros_matrix(rows, cols):
    M = []
    for i in range(rows):
        M.append([])
        for j in range(cols):
            M[-1].append(0.0)

    return M

def identity_matrix(n):
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M):
    for row in M:
        print([round(x,3)+0 for x in row])

def transpose(M):
    rows = len(M)
    cols = len(M[0])

    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print ('Number of A columns must equal number of B rows.')
        sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def inverse_matrix(A):
    check_squareness(A)

    n = len(A)
    AM = copy_matrix(A)
    Inv = identity_matrix(n)

    # Make the lower triangular matrix all 0’s and make all diagonal elements 1’s
    for fd in range(n): # fd is for focus diagonal
        for i in range(fd,n):
            if i == fd:
                scaler = 1.0 / AM[i][fd]
            else:
                scaler = AM[i][fd]
            for j in range(n):
                if i == fd:
                    AM[i][j] *= scaler
                    Inv[i][j] *= scaler
                else:
                    AM[i][j] = AM[i][j] - scaler * AM[fd][j]
                    Inv[i][j] = Inv[i][j] - scaler * Inv[fd][j]

    # Make the upper triangular matrix all 0’s
    for fd in range(n-1,0,-1):
        for i in range(fd-1,-1,-1):
            scaler = AM[i][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - scaler * AM[fd][j]
                Inv[i][j] = Inv[i][j] - scaler * Inv[fd][j]

    return Inv
