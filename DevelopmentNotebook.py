#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def print_matrices(Action, Title1, M1, Title2, M2):
    print(Action)
    print(Title1, '\t'*int(len(M1)/2)+"\t"*len(M1), Title2)
    for i in range(len(M1)):
        row1 = ['{0:+7.3f}'.format(x) for x in M1[i]]
        row2 = ['{0:+7.3f}'.format(x) for x in M2[i]]
        print(row1,'\t', row2)
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


# In[2]:


A = [[5.,3.,1.],[3.,9.,4.],[1.,3.,5.]]
I = [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]

print('A and I are our starting matrices.')
Action = ''
print_matrices(Action, 'A Matrix', A, 'I Matrix', I)


# In[3]:


AM = copy_matrix(A)
IM = copy_matrix(I)
n = len(AM)

exString = """
Since the matrices won't be the original A and I as we start row operations, 
    the matrices will be called: AM for "A Morphing", and IM for "I Morphing" 
"""
print_matrices(exString, 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[9]:


# Run this cell then the next for fd = 0, 1, and 2 for a 3x3 matrix. 
#      Then check for identity matrix in last cell.

fd = 2 # fd stands for focus diagonal OR the current diagonal
fdScaler = 1. / AM[fd][fd]

for j in range(n): # using j to indicate cycling thru columns
    AM[fd][j] = fdScaler * AM[fd][j]
    IM[fd][j] = fdScaler * IM[fd][j]
    
print()
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)


# In[10]:


n = len(A)
indices = list(range(n))

for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
    crScaler = AM[i][fd] # cr stands for "current row".
    for j in range(n): # cr - crScaler * fdRow, but one element at a time.
        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[11]:


print_matrix('Identity Matrix from A * Ainv', matrix_multiply(A,IM))


# In[ ]:




