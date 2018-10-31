#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_matrix(M):
    for row in M:
        print([round(x,3)+0 for x in row])


# In[2]:


A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
print_matrix(A)
print()
I = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
print_matrix(I)


# In[3]:


fd = 0 # fc = focus column

scaler = 1.0 / A[fd][fd]

for j in range(fd, len(A[fd])): # use j when we cycle thru columns
    A[fd][j] *= scaler
    I[fd][j] *= scaler
    
print_matrix(A)
print()
print_matrix(I)


# In[4]:


for i in range(fd+1,len(A)):
    scaler = A[i][fd]
    for j in range(fd,len(A[fd])):
        A[i][j] = A[i][j] - scaler * A[fd][j]
        I[i][j] = I[i][j] - scaler * I[fd][j]
        
print('fd:',fd)
print_matrix(A)
print()
print_matrix(I)
print()


# In[5]:


for fd in range(1,5): # fd = focus diagonal

    scaler = 1.0 / A[fd][fd]

    for j in range(len(A[fd])): # use j when we cycle thru columns
        A[fd][j] *= scaler
        I[fd][j] *= scaler

    for i in range(fd+1,len(A)):
        scaler = A[i][fd]
        for j in range(len(A[fd])):
            A[i][j] = A[i][j] - scaler * A[fd][j]
            I[i][j] = I[i][j] - scaler * I[fd][j]

    print('fd:',fd)
    print_matrix(A)
    print()
    print_matrix(I)
    print()


# In[6]:


fd = 4 # fd = focus diagonal

for i in range(fd-1, -1, -1):
    scaler = A[i][fd]
    for j in range(len(A[fd])):
        A[i][j] = A[i][j] - scaler * A[fd][j]
        I[i][j] = I[i][j] - scaler * I[fd][j]

print('fd:',fd)
print_matrix(A)
print()
print_matrix(I)
print()


# In[7]:


for fd in range(3,0,-1): # fd = focus diagonal

    for i in range(fd-1, -1, -1):
        scaler = A[i][fd]
        for j in range(len(A[fd])):
            A[i][j] = A[i][j] - scaler * A[fd][j]
            I[i][j] = I[i][j] - scaler * I[fd][j]

    print('fd:',fd)
    print_matrix(A)
    print()
    print_matrix(I)
    print()


# In[8]:


def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

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


# In[9]:


A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
print_matrix(matrix_multiply(A,I))

