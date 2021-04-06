from collections import Counter

def solution(participant, completion):
    
    part = Counter(participant)
    comple = Counter(completion)
    
    set_ = set(part.keys()) - set(comple.keys())
    
    answer = ''
    
    if(len(set_) == 1):
        answer = list(set_)[0]
    else:
        for i in list(part.keys()):
            if(part[i] - comple[i] == 1):
                answer = i
    return answer
