def matmul(A, B):
    if len(A[0]) != len(B):
        return None
    matprod = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                matprod[i][j] += A[i][k] * B[k][j]
    return matprod 
