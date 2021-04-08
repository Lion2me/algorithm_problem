import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    end = [0 for i in range(len(progresses))]
    
    for i in range(len(progresses)):
        end[i] = math.ceil((100 - progresses[i])/speeds[i])
    
    end = deque(end)
    now = end[0]

    term = 0
    for i in range(len(end)):
        if(end[i] <= now):
            term += 1
        else:
            answer.append(term)
            now = end[i]
            term = 1
        if(i == len(end)-1):
            answer.append(term)

    
    return answer
