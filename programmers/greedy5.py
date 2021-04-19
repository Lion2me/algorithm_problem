from collections import defaultdict, deque
def solution(n, costs):
    answer = 0
    
    graph = defaultdict(list)
    
    dist_ = [-1 for i in range(n)]
    dist_[0] = 0
    
    for start,end,score in costs:
        graph[start].append([end,score])
        graph[end].append([start,score])
    
    tmp = []
    for start,end,score in costs:
        tmp.append([end,start,score])
    
    stack_ = deque(sorted(graph[0],key = lambda x:x[1]))
    while(stack_):
        en,score = stack_.popleft()
        if(dist_[en] == -1):
            dist_[en] = score
            stack_.extend(graph[en])
            stack_ = deque(sorted(stack_,key = lambda x:x[1]))
    
    answer = sum(dist_)
    
    return answer
