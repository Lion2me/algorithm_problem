def solution(answers):
    
    a = []
    a.append([1,2,3,4,5] * 2001)
    a.append([2,1,2,3,2,4,2,5] * 1300)
    a.append([3,3,1,1,2,2,4,4,5,5] * 1001)
    
    answer = []
    count = [0,0,0]
    
    for ans_idx in range(len(answers)):
        for i in range(len(a)):
            if(a[i][ans_idx] == answers[ans_idx]):
                count[i] += 1
    max_ = max(count)
    
    for i in range(len(count)):
        if count[i] == max_:
            answer.append(i+1)
    
    
    return answer
