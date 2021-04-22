from collections import deque

board_tmp = []
board_copy = []
n = 0
stat_list = [[100,600,100,600],[600,100,600,100]]
def dfs(y,x,stat):
    list_ = []
    if( stat == 0):
        list_ = stat_list[0]
    else:
        list_ = stat_list[1]
    if(y+1 < n and board_copy[y+1][x] != 1 and board_tmp[y+1][x] > board_tmp[y][x] + list_[0]):
        board_tmp[y+1][x] = board_tmp[y][x] + list_[0]
        dfs(y+1,x,0)
    if(x+1 < n and board_copy[y][x+1] != 1 and board_tmp[y][x+1] > board_tmp[y][x] + list_[1]):
        board_tmp[y][x+1] = board_tmp[y][x] + list_[1]
        dfs(y,x+1,1)
    if(y-1 >= 0 and board_copy[y-1][x] != 1 and board_tmp[y-1][x] > board_tmp[y][x] + list_[2]):
        board_tmp[y-1][x] = board_tmp[y][x] + list_[2]
        dfs(y-1,x,0)
    if(x-1 >= 0 and board_copy[y][x-1] != 1 and board_tmp[y][x-1] > board_tmp[y][x] + list_[3]):
        board_tmp[y][x-1] = board_tmp[y][x] + list_[3]
        dfs(y,x-1,1)


def solution(board):
    answer = 0
    global board_tmp , n , board_copy
    n = len(board)
    board_copy = board
    board_tmp = [[99999999] * n for i in range(len(board))]
    board_tmp[0][0] = 0
    
    dfs(0,0,1)
    dfs(0,0,0)
    
    min_board_tmp = board_tmp[n-1][n-1]
    
    board_tmp = [[99999999] * n for i in range(len(board))]
    board_tmp[0][0] = 0
    
    dfs(0,0,0)
    dfs(0,0,1)
    
    min_board_tmp = min(min_board_tmp, board_tmp[n-1][n-1])
    
    answer = min_board_tmp
    
    return answer
