def solution(array, commands):
    
    answer=[]
    for st,end,index in commands:
        tmp = array[st-1:end]
        tmp = sorted(tmp)
        answer.append(tmp[index-1])
    
    return answer
