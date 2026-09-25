def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # first define 2d matrix with m*n 
    m = 0
    n = 0
    # matrix = [[0 for _ in range(m)] for _ in range(n)]
    arr = []
    miniArr = []
    while n < len(a) and m < len(a[n]):
        miniArr.append(a[n][m])
        n += 1
        if n == len(a):
            arr.append(miniArr)
            miniArr = []
            n = 0
            m += 1
            
    return arr