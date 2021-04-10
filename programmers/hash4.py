import heapq
from collections import defaultdict
def solution(genres, plays):
    
    heap_ = []
    answer = []
    dict_ = defaultdict(list)
    dict_max = defaultdict(int)
    
    for i in range(len(genres)):
        dict_[genres[i]].append((-plays[i],plays[i],i))
        
    for i in dict_.keys():
        heapq.heapify(dict_[i])
        dict_max[i] = sum(list(map(lambda x:x[1],dict_[i])))
    
    sort_key = sorted(dict_max.items() , key=lambda x:x[1])[::-1]
    
    for gen,num in sort_key:
        for i in range(2):
            if(dict_[gen]):
                a = heapq.heappop(dict_[gen])
                answer.append(a[2])
        
        
    return answer
