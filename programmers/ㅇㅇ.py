def solution(priorities, location):
    
    ans = []
    
    seq = [i for i in range(len(priorities))]
    
    while priorities:
        index = priorities.index(max(priorities))
        ans.append(seq[index])
        seq = seq[index+1:] + seq[:index]
        priorities = priorities[index+1:] + priorities[:index]
    answer = ans.index(location)+1
    return answer
