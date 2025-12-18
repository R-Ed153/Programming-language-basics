def matrixChain(d):
    n = len(d) -1
    N = [[0]*n for i in range(n)]
    for b in range(1,n):
        for i in range(n-b):
            j = i+b
            N[i][j] = min(N[i][k]+N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i,j))
    return N