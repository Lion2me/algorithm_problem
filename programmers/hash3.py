from collections import Counter
def solution(clothes):
    
    answer = 0
    
    clothes = [i[1] for i in clothes]
    
    dict_ = Counter(clothes)
    
    keys = list(dict_.keys())
    values = list(dict_.values())
    num = 1
    for i in values:
        num = num * (i+1)
    answer = num-1
    
    return answer
