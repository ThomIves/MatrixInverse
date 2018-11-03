import LinearAlgebraPurePython as la 


print()
A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
la.print_matrix(A)
print()

Inv = la.inverse_matrix(A)
la.print_matrix(Inv)
print()

C = la.matrix_multiply(A, Inv)
la.print_matrix(C)
print()
