from itertools import combinations
from collections import defaultdict , Counter
def solution(orders, course):
    answer = []
    
    dict_ = defaultdict(list)
    
    for i in orders:
        for cour in course:
            comb = list(map(lambda x:''.join(sorted(list(x))) ,list(combinations(i,cour))))
            dict_[cour].extend(comb)
    
    for i in course:
        tmp = dict(Counter(dict_[i]))
        if(len(tmp.keys()) == 0):
            continue
        max_ = max(tmp.values())
        if(max_ < 2):
            continue
        for key, value in tmp.items():
            if(value == max_):
                answer.append(key)
    answer = sorted(answer)
    return answer
