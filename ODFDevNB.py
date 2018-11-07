#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def get_ODF(Action, Title1, M1, Title2, M2):
    topString = 'alignc'+Action+'\n newline newline'
    topString += '\nalignc"'+Title1+' '*(28)+Title2+'"'
    topString += '\nnewline'
    
    m1String = '\nleft[matrix{'
    m2String = '\nleft[matrix{'
    
    for i in range(len(M1)):
        row1 = ['{:.3f}'.format(x) for x in M1[i]]
        m1String += ' # '.join(row1)
        m1String += ' ## '
        
        row2 = ['{0:.3f}'.format(x) for x in M2[i]]
        m2String += ' # '.join(row2)
        m2String += ' ## '
        
    m1String = m1String.rstrip(' ## ')
    m1String += '} right]'
    
    m2String = m2String.rstrip(' ## ')
    m2String += '} right]'
    
    return topString + m1String + '~~~~~~~' + m2String + '\nnewline newline\n'

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

ODF_String = ''
ODF_String += get_ODF('""', 'A Matrix', A, 'I Matrix', I)


# In[3]:


AM = copy_matrix(A)
IM = copy_matrix(I)
n = len(AM)

exString = """ "Our starting matrices are:" """
ODF_String += get_ODF(exString, 'AM Matrix', AM, 'IM Matrix', IM)
# print(ODF_String)


# In[4]:


indices = list(range(n)) # to allow flexible row referencing ***
for fd in range(n): # fd stands for focus diagonal
    fdScaler = 1.0 / AM[fd][fd]
    # FIRST: scale fd row with fd inverse. 
    for j in range(n): # Use j to indicate column looping.
        AM[fd][j] *= fdScaler
        IM[fd][j] *= fdScaler
    
    # Section to grow ODF string:
    ActionString = '"Scale row {} of both matrices by 1/{}:"'.format(fd+1, round(1/fdScaler,3))
    ODF_String += get_ODF(ActionString, 'AM Matrix', AM, 'IM Matrix', IM)
    # print(ODF_String)
    
    
    # SECOND: operate on all rows except fd row.
    for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
        crScaler = AM[i][fd] # cr stands for "current row".
        for j in range(n): # cr - crScaler * fdRow, but one element at a time.
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
        
        # Section to grow ODF string:
        ActionString = '"Subtract {} * row {} of A from row {} of A"\nnewline\n'.format(round(crScaler,3),i,i+1)
        ActionString += 'alignc"Subtract {} * row {} of I from row {} of I"'.format(round(crScaler,3),i,i+1)
        ODF_String += get_ODF(ActionString, 'AM Matrix', AM, 'IM Matrix', IM)
        # print(ODF_String)


# In[5]:


print(ODF_String)


# In[6]:


print_matrix('Identity Matrix from A * Ainv', matrix_multiply(A,IM))

