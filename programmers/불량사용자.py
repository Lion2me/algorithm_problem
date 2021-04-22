from collections import defaultdict


dict_ = defaultdict(list)
list_ = []
def dfs(stack_, cnt):
    if(len(dict_[cnt]) == 0):
        list_.append(stack_)
        return
    for i in dict_[cnt]:
        stack_ = stack_[:cnt]
        if(i not in stack_):
            stack_.append(i)
            dfs(stack_,cnt+1)

def solution(user_id, banned_id):
    answer = 0
    
    
    global dict_ , list_
    cnt = 0
    for ban_id in banned_id:
        for user in user_id:
            if(len(ban_id) == len(user)):
                tmp = True
                for i in range(len(user)):
                    if(user[i] != ban_id[i] and ban_id[i] != '*'):
                        tmp = False
                if(tmp == True):
                    dict_[cnt].append(user)
        cnt += 1
    dfs([],0)
    
    for i in range(len(list_)):
        list_[i] = '-'.join(sorted(list_[i]))
    answer = len(set(list_))
    return answer
