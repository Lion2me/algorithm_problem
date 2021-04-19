import heapq
def solution(routes):
    
    for i in range(len(routes)):
        if(routes[i][0] > routes[i][1]):
            routes[i] = [routes[i][1],routes[i][0]]
    
    routes = sorted(routes,key=lambda x:(x[0] , x[1]))
    
    outs = [30001]
    heapq.heapify(outs)
    
    answer= 1
    
    for st,en in routes:
        if(outs[0] >= st):
            heapq.heappush(outs,en)
        elif(outs[0] <= st):
            outs = [30001]
            heapq.heappush(outs,en)
            answer += 1
    
    return answer
