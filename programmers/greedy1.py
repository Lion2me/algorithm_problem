def solution(n, lost, reserve):
    answer = 0
    
    students = [ 1 for i in range(n+1)]
    
    for i in range(len(lost)):
        students[lost[i]] = students[lost[i]]-1
    for i in range(len(reserve)):
        students[reserve[i]] = students[reserve[i]]+1
    
    students[0] = 1
    
    for i in range(1,n+1):
        if(students[i] == 2):
            if(students[i-1] == 0):
                students[i-1] = 1
                students[i] = 1
            elif(i != n and students[i+1] == 0):
                students[i+1] = 1
                students[i] = 1
            else:
                students[i] = 1
                continue
                
    answer = len(list(filter(lambda x:x>0,students[1:])))
    
    return answer
