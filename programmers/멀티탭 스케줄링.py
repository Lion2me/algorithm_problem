from collections import deque

n,k = [int(n) for n in input().split()]
use = [int(n) for n in input().split()]

def solution(n,k,use):
    now_ = []
    now_k = 0
    use = deque(use)
    answer = 0
    while(use):
        item = use.popleft()
        if(item in now_):
            continue
        elif(now_k < n):
            now_.append(item)
            now_k += 1
        else:
            min_idx = -1
            tmp = False
            for i in now_:
                try:
                    min_idx = max(use.index(i),min_idx)
                except:
                    now_.remove(i)
                    now_.append(item)
                    tmp = True
                    answer += 1
                    break
            if(tmp==False and min_idx != -1):
                now_.remove(use[min_idx])
                now_.append(item)
                answer += 1
    return answer

print(solution(n,k,use))
