#!/usr/bin/env python
# coding: utf-8

# ![Matrix Inversion Logo](Matrix_Inverse_Logo.png)
# # Dirt Simple Matrix Inversion
# [MatrixInversion on Github](https://github.com/ThomIves/MatrixInverse)

# We are going to walk thru a brute force procedural method for inverting a matrix with pure Python. Why wouldn’t we just use numpy? Great question. This blog is about tools that add efficiency **_AND_** _clarity_. I love numpy, pandas, sklearn, and all the great tools that the python data science community brings to us, but I have learned that the better I understand the “innards” of a thing, the better I know how to apply it. Plus, *tomorrows machine learning tools will be developed by those that understand the **principles** of the math and coding of today’s tools.* 
# 
# Also, once an efficient method of matrix inversion is understood, you are ~ 80% of the way to having your own Least Squares Solver and a component to many other personal analysis modules to help you better understand how all our great machine learning tools are built. Would I recommend that you use what we are about to develop for a real project? All those python modules mentioned previously are lightening fast, so, usually, no. I would not recommend that you use your own such tools **UNLESS** you are working with smaller problems, **OR** you are investigating some new approach that requires slight changes to your personal tool suite. Thus, a statement above bears repeating: *tomorrows machine learning tools will be developed by those that understand the **principles** of the math and coding of today’s tools.* I want to be part of, or at least foster, those that will make the next gen tools. Plus, if you are a geek, knowing how to code the inversion of a matrix is fun!
# 
# The way I was taught to inverse matrices, *in the dark ages that is*, was pure torture! If you go about it the way that you would program it, it is MUCH easier in my opinion. I would even think it’s easier doing the method we will use when doing it by hand than the ancient teaching of how to do it. In fact, it is so easy that we will start with a 5x5 matrix to make it “clearer”.
# 
# **DON’T PANIC.** The only really painful thing about it, is that, while it’s very simple, it’s a bit tedious and boring. However, compared to the ancient method, it’s simple. Or, as one of my favorite mentors would commonly say, “It’s simple. it’s just not easy.” We’ll use python, to reduce the tedium, without losing any view to the insights of the methods.
# 
# We’ll use python at first through a Jupyter notebook to clearly illustrate each step. Then, we’ll be VERY ready to adapt those steps to build our own module. I will seek to be very pep8’ish. Please deviate from my style as you wish to make what we are doing your own and more clear to you. You’ll be glad that you did.
# 
# The logo for the github repo that stores all this work, really says it all.
# 
# Following the main rule of algebra (whatever we do to one side of the equal sign, we will do to the other side of the equal sign, in order to “stay true” to the equal sign), we will perform row operations to **A** in order to methodically turn it into an identity matrix while applying those same steps to what is “initially” the identity matrix on the right. 
# 
# When what was __A__ becomes an identity matrix, what was I on the right will become **A-1**. 
# 
# If at some point, you have a big **“Ah HA!”** moment, try to work ahead on your own and compare to what we’ve done once you’ve finished or if you get stuck. 
# 
# The Jupyter notebook called **MatrixInversion.ipynb** can be obtained from the [github repo](https://github.com/ThomIves/MatrixInverse) for this project. You don’t need to use Jupyter to follow along. I’ve also saved the cells as MatrixInversion.py in the same repo. Let’s first define some helper functions.

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


# **NOTE:** The last print statement uses a trick to get rid of -0.0’s. Try it with and without the “+0” to see what I mean.
# 
# Let’s prepare some matrices to use.

# In[2]:


A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
I = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
print_matrices('','A Matrix', A, 'I Matrix', I)


# Let's make some copies that we can morph while preserving our originals

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


# The first basic step, consider the first element of the diagonal of **A**, which is __5__. Let's divide all elements of the first row by it. 
# 
# From here forward, all operations applied to **A**, also are applied to __I__.

# In[4]:


# Run this cell then the next for fd = 0, 1, 2, 3, and 4 for a 5x5 matrix. 
#      Then check for identity matrix in last cell.

fd = 0 # fd stands for focus diagonal OR the current diagonal
fdScaler = 1. / AM[fd][fd]

for j in range(n): # using j to indicate cycling thru columns
    AM[fd][j] = fdScaler * AM[fd][j]
    IM[fd][j] = fdScaler * IM[fd][j]
    
print()
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)


# Now we do the following: 
# 1. look at the rows below the focus diagonal element that we just scaled; 
# 2. for each of those rows, use the element below the current focus diagonal as a scaler;
# 3. replace each row with the result of [current row] - scaler*[row with focus diagonal];
# 4. This leaves zeros in the column below the focus diagonal element, which was previously scaled to 1.
# 
# If you’re as big a geek as me, you have chills now.

# In[5]:


n = len(A)
indices = list(range(n))

for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
    crScaler = AM[i][fd] # cr stands for "current row".
    for j in range(n): # cr - crScaler * fdRow, but one element at a time.
        AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
        IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    
print_matrices('', 'AM Matrix', AM, 'IM Matrix', IM)
print()


# We focus on the next diagonal element of our morphing **A** matrix, and repeat the above steps. However, this time, we do the operations on all rows above and below the focus diagonal. Thus, we divide the second row by -0.2. Then, like before, but using the second row now, we 
# 
# 1. look at the rows above and below the row that the focus diagonal is in; 
# 2. for each of those rows, use the elements above and below the current focus diagonal as a scaler;
# 3. replace each row with the result of [current row] - scaler*[row with focus diagonal];
# 4. This leaves zeros in the column above and below the focus diagonal element, which was scaled to 1 previously.
# 
# Move from left to right and repeat this process. Doing so will make all the diagonal elements 1, and all the elements of the upper and lower triangles 0. 
# 
# Remember, EVERYTHING that we’re doing to the morphing __A__ matrix must be done to the morphing **I** matrix too. 
# 
# If we don’t, the __I__ matrix will not become the inverse of **A**.

# In[6]:


indices = list(range(n)) # to allow flexible row referencing ***
for fd in range(1,n): # fd stands for focus diagonal
    fdScaler = 1.0 / AM[fd][fd]
    # FIRST: scale fd row with fd inverse. 
    for j in range(n): # Use j to indicate column looping.
        AM[fd][j] *= fdScaler
        IM[fd][j] *= fdScaler
    
    # Section to print out current actions:
    string1 = '\nUsing the matrices above, Scale row-{} of AM and IM by '
    string2 = 'diagonal element {} of AM, which is 1/{:+.3f}.\n'
    stringsum = string1 + string2
    val1 = fd+1; val2 = fd+1
    Action = stringsum.format(val1,val2,round(1./fdScaler,3))
    print_matrices(Action, 'AM Matrix', AM, 'IM Matrix', IM)
    print()
    
    # SECOND: operate on all rows except fd row.
    for i in indices[:fd] + indices[fd+1:]: # *** skip row with fd in it.
        crScaler = AM[i][fd] # cr stands for "current row".
        for j in range(n): # cr - crScaler * fdRow, but one element at a time.
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
        
        # Section to print out current actions:
        string1 = 'Using the matrices above, subtract {:+.3f} * row-{} of AM from row-{} of AM, and \n'
        string2 = '\tsubtract {:+.3f} * row-{} of IM from row-{} of IM\n'
        val1 = i+1; val2 = fd+1
        stringsum = string1 + string2
        Action = stringsum.format(crScaler, val2, val1, crScaler, val2, val1)
        print_matrices(Action, 'AM Matrix', AM, 'IM Matrix', IM)
        print()


# Success! 
# 
# **A** has morphed into an Identity matrix. 
# 
# **I** has become the inverse of __A__. 
# 
# Yay! And yes, I am easily entertained. 

# Let’s apply some helper functions to accomplish proof of inversion.

# In[7]:


A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
print_matrix('Proof of Inversion', matrix_multiply(A,IM))


# Yes! When we multiply the original A matrix on our Inverse matrix we do get the identity matrix. 
# 
# I do love Jupyter notebooks, but I want to use this in scripts now too. See LinearAlgebraPurePython.py and a file that uses it - LinearAlgebraPractice.py.

# In[ ]:




