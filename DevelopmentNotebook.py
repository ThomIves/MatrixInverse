#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


A = [[5.,3.,1.],[3.,9.,4.],[1.,3.,5.]]
I = [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]

print('A and I are our starting matrices.')
Action = ''
print_matrices(Action, 'A Matrix', A, 'I Matrix', I)


# In[ ]:


AM = copy_matrix(A)
IM = copy_matrix(I)
n = len(AM)

exString = """
Since the matrices won't be the original A and I as we start row operations, 
    the matrices will be called: AM for "A Morphing", and IM for "I Morphing" 
"""
print_matrices(exString, 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


diagonal = 0
scaler = 1. / AM[diagonal][diagonal]

row = diagonal
for column in range(len(AM[row])):
    AM[row][column] = scaler * AM[row][column]
    IM[row][column] = scaler * IM[row][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


row = 1
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


row = 2
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


diagonal = 1
scaler = 1. / AM[diagonal][diagonal]

row = diagonal
for column in range(len(AM[row])):
    AM[row][column] = scaler * AM[row][column]
    IM[row][column] = scaler * IM[row][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


row = 2
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


diagonal = 2
scaler = 1. / AM[diagonal][diagonal]

row = diagonal
for column in range(len(AM[row])):
    AM[row][column] = scaler * AM[row][column]
    IM[row][column] = scaler * IM[row][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


row = 1
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


row = 0
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


diagonal = 1
row = 0
scaler = AM[row][diagonal]
for column in range(len(AM[row])):
    AM[row][column] = AM[row][column] - scaler * AM[diagonal][column]
    IM[row][column] = IM[row][column] - scaler * IM[diagonal][column]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# In[ ]:


print_matrix('Identity Matrix from A * Ainv', matrix_multiply(A,IM))


# In[ ]:




