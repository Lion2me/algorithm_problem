from collections import defaultdict
def solution(msg):
    answer = []
    alpha_set = [chr(i+65) for i in range(26)]
    now_idx = 27
    dict_ = defaultdict(int,{key:num+1 for num,key in enumerate(alpha_set)})
    
    while(True):
        if(dict_[msg] != 0):
            answer.append(dict_[msg])
            break
        for i in range(1,len(msg)+1):
            if(dict_[msg[:i]] == 0):
                answer.append(dict_[msg[:i-1]])
                dict_[msg[:i]] = now_idx
                now_idx += 1
                msg = msg[i-1:]
                break

    return answer
