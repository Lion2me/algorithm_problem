from copy import deepcopy
def solution(triangle):
    triangle_tmp = deepcopy(triangle)
    
    for i in range(len(triangle)):
        if(i == len(triangle) - 1):
            break
        for j in range(len(triangle[i])):
            tmp = triangle_tmp[i][j]
            if(triangle_tmp[i+1][j] < tmp + triangle[i+1][j]):
                triangle_tmp[i+1][j] = tmp + triangle[i+1][j]
            if(triangle_tmp[i+1][j+1] < tmp + triangle[i+1][j+1]):
                triangle_tmp[i+1][j+1] = tmp + triangle[i+1][j+1]
    answer = 0
    for i in triangle_tmp:
        if(answer < max(i)):
            answer = max(i)
    
    return answer
