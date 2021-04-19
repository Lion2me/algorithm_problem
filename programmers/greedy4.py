from collections import deque

def solution(people, limit):
    answer = 0
    
    people = deque(sorted(people))
    
    left = 0
    
    while(people):
        max_ = people.pop()
        if people:
            min_ = people[0]
            if(max_ + min_ <= limit):
                people.popleft()

        answer += 1
        
    return answer
