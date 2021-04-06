
import heapq

def solution(jobs):
    count = len(jobs)
    heapq.heapify(jobs)
    use_heap = []
    times = []
    time = 0
    
    status = False
    while(len(jobs) >= 1 or len(use_heap) > 0):
        while(jobs and jobs[0][0] <= time):
            heapq.heappush(use_heap , heapq.heappop(jobs)[::-1])
        if(len(use_heap) > 0):
            tmp = heapq.heappop(use_heap)
            times.append(tmp[0]+time - tmp[1])
            time += tmp[0]
        else:
            time += 1
    
    answer = int(sum(times)/count)

    return answer
