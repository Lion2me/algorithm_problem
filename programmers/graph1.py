from collections import defaultdict,deque
def solution(n, edge):
    
    graph = defaultdict(list,{key : [] for key in range(1,n+1)})
    
    for idx,value in edge:
        graph[idx].append(value)
        graph[value].append(idx)
    
    graph_ans = defaultdict(int,{ key : 50001 for key in range(1,n+1)})
    visited = [0 for i in range(n+1)]
    visited[1] = 1
    queue = deque([(1,0)])
    
    graph_ans[1] = -1
    
    while queue:
        now, now_dist = queue.popleft()
        
        dest_list = graph[now]
        for dest in dest_list:
            if(visited[dest] == 0):
                visited[dest] = 1
                graph_ans[dest] = now_dist+1
                queue.append((dest,now_dist+1))
                
    max_ = max(graph_ans.values())
    
    answer = len(list(filter(lambda x:x == max_,graph_ans.values())))
    
    
    
    return answer
