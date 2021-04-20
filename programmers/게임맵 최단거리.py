from collections import deque
from copy import deepcopy

def solution(maps):
    answer = 0
    
    visited = [[99999999] * len(maps[0]) for i in range(len(maps))]
    
    now_ = deque([[0,0]])
    visited[0][0] = 1
    while(now_):
        if(visited[len(maps)-1][len(maps[0])-1] != 99999999):
            break
        y,x = now_.popleft()
        if(y+1 < len(maps) and maps[y+1][x] == 1 and visited[y+1][x] == 99999999):
            visited[y+1][x] = visited[y][x]+1
            now_.append([y+1,x])
        if(x+1 < len(maps[0]) and maps[y][x+1] == 1 and visited[y][x+1] == 99999999):
            visited[y][x+1] = visited[y][x]+1
            now_.append([y,x+1])
        if(y-1 >= 0 and maps[y-1][x] == 1 and visited[y-1][x] == 99999999):
            visited[y-1][x] = visited[y][x]+1
            now_.append([y-1,x])
        if(x-1 >= 0 and maps[y][x-1] == 1 and visited[y][x-1] == 99999999):
            visited[y][x-1] = visited[y][x]+1
            now_.append([y,x-1])
        
    answer = visited[len(maps)-1][len(maps[0])-1]
    if(answer == 99999999):
        answer = -1
    return answer
