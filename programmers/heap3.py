
import heapq

def solution(operations):
    answer = []
    
    min_list = []
    max_list = []

    idx = 0
    leng = 0
    for oper in operations:
        op, num = oper.split(' ')
        if(op == 'I'):
            heapq.heappush(min_list,int(num))
            heapq.heappush(max_list,-int(num))
            leng += 1
        if(op == 'D'):
            if(leng == 0):
                continue
            if(num == '1'):
                heapq.heappop(max_list)
                leng -= 1
            elif(num == '-1'):
                heapq.heappop(min_list)
                leng -= 1
            if(leng == 0):
                max_list = []
                min_list = []

    if (leng == 0):
        answer = [0,0]
    else:
        answer = [-min(max_list),min(min_list)]
    
    return answer
