def solution(m, n, puddles):
    answer = 0
    
    board = [[1] * (102) for q in range(102)]
    
    for y, x in puddles:
        board[y][x] = 0
    
    for i in range(len(board)):
        board[i][0] = 0
    for j in range(len(board[0])):
        board[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(board[i][j] == 0):
                continue
            if(i== 1 and j == 1):
                continue
            if(board[i-1][j] != 0 and board[i][j-1] != 0):
                board[i][j] = board[i-1][j] + board[i][j-1]
                board[i][j] %= 1000000007
            else:
                board[i][j] = max(board[i-1][j] , board[i][j-1])

    answer = board[m][n]
    return answer
