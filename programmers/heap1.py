
import heapq

def solution(scoville, K):
    
    answer = 0
    
    heapq.heapify(scoville)
    num = heapq.heappop(scoville)
    
    while( num < K ):
        
        if(len(scoville) < 1):
            answer = -1
            break
            
        next_num = num + heapq.heappop(scoville) * 2
        heapq.heappush(scoville,next_num)
        num = heapq.heappop(scoville)
        
        answer += 1
    
    return answer
