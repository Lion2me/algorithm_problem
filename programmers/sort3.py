from collections import Counter
import numpy as np
def solution(citations):
    
    citations = np.array(sorted(citations))
    
    for i in range(10001):
        count = len(citations[citations > i])
        if( i > count):
            break
        elif( i <= count):
            continue
    if(len(np.where(citations == i)[0]) != 0):
        answer = i
    else:
        answer = i-1
    
    return answer
