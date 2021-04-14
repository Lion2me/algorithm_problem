def solution(name):
    answer = 0
    
    now_name = ['A' for i in range(len(name))]
    
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_length = len(alpha)
    name_length = len(name)
    
    # name에서 A가 아닌 지점으로 -방향 +방향 가장 가까운 곳으로 이동
    # alpha는 갯수를 잘 나누면 할만할듯
    idx = 0
    while(''.join(now_name) != name):
        now_name[idx] = name[idx]
        answer += min([alpha.index(name[idx]),alpha_length-alpha.index(name[idx])])
        dist = [min([i-idx,name_length - i + idx]) for i in range(len(name)) if name[i] != 'A' and now_name[i] == 'A']
        if(dist):
            next_move = min(dist)
            if(now_name[idx + next_move] == 'A' and name[idx+next_move] != 'A'):
                idx = idx+next_move
                answer += next_move
            elif(now_name[idx - next_move] == 'A' and name[idx-next_move] != 'A'):
                idx = idx-next_move
                answer += next_move
        # 가장 가까운 A가 아닌 단어 찾기
    
    dist = [min([i - idx, name_length - i - idx]) for i in range(len(name)) if name[i] != 'A']
    return answer
