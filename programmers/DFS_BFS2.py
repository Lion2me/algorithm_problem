map_ = 0
max_n = 0
t = 2

from functools import reduce
from collections import defaultdict , deque

def solution(n, computers):
    answer = 0
    
    visited = [0 for i in range(n)]
    
    dict_ = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if(computers[i][j] == 1):
                dict_[i].append(j)
                dict_[j].append(i)
    
    for key in dict_.keys():
        dict_[key] = list(set(dict_[key]))
    
    for i in range(n):
        if(visited[i] == 0):
            answer += 1
            queue = deque([i])
            while(queue):
                net = queue.popleft()
                if(visited[net] == 0):
                    visited[net] = 1
                    queue.extend(dict_[net])
                else:
                    continue
        else:
            continue
        
    return answer
