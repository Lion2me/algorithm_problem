from copy import deepcopy

def solution(m, n, board):
    answer = 0
    
    board = [list(x) for x in board]
    tmp = []
    while(True):
        for i in range(m-1):
            for j in range(n-1):
                button = board[i][j]
                if(button != '_' and board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1] ):
                    tmp.append([i,j])
                    tmp.append([i+1,j])
                    tmp.append([i+1,j+1])
                    tmp.append([i,j+1])
        if(len(tmp) == 0):
            break
        
        for y,x in tmp:
            board[y][x] = '_'
        tmp = []
        for j in range(n):
            board_tmp = list(map(lambda x:x[j] , board))
            board_tmp = list(filter(lambda x:x != '_', board_tmp))
            board_tmp = ['_'] * (m - len(board_tmp)) + board_tmp
            for i in range(m):
                board[i][j] = board_tmp[i]
                
    for i in board:
        answer += len(list(filter(lambda x:x == '_' , i)))
    return answer
