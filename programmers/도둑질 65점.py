from copy import deepcopy
def solution(money):
    answer = 0
    
    visited = [0 for i in range(len(money))]
    
    is_first = [False for i in range(len(money))]
    
    is_first[0] = True
    
    visited = deepcopy(money)
        
    if(len(money) == 3):
        return max(money)
    if(len(money) == 4):
        return max(money[0] + money[2] , money[1]+money[3])
    
    
    for i in range(2,len(money)):
        if(i == 2):
            if(visited[i-2] + money[i] < visited[i-3] + money[i]):
                continue
            else:
                visited[i] = visited[i-2] + money[i]
        if(visited[i-2]+money[i] >= visited[i-3] + money[i]):
            if(is_first[i-2] == True):
                is_first[i] = True
                if(i == len(money)-1):
                    continue
            visited[i] = visited[i-2] + money[i]
        else:
            if(is_first[i-3] == True):
                is_first[i] = True
                if(i == len(money)-1):
                    continue
                if(i == len(money)-2 and is_first[-1] == True):
                    continue
            visited[i] = visited[i-3] + money[i]

    answer = max(visited)
    return answer
