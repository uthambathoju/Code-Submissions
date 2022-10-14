def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    table = [[0]*n for _ in range(m)]
    for i in range(n):
        table[0][i] = 1
    for j in range(m):
        table[j][0] = 1
    for i in range(1,m):
        for j in range(1,n):
            table[i][j] = table[i-1][j] + table[i][j-1]
    return table[m-1][n-1]
