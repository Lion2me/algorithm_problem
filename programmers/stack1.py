from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    arrive = 0
    wait = deque(truck_weights)
    num = len(truck_weights)
    now = deque()
    now_weight = 0
    
    while True:
        if(arrive == num):
            break
        if(now and now[0][1] <= time):
            now_weight -= now[0][0]
            now.popleft()
            arrive += 1
        if(wait and weight >= now_weight + wait[0]):
            now_weight += wait[0]
            now.append([wait.popleft(),time + bridge_length])
        
        time += 1
    
    return time
