from collections import defaultdict
def solution(begin, target, words):
    
    words.append(begin)
    
    dict_ = defaultdict(list)
    
    ans_dict = defaultdict(int,{key : 999999999 for key in words})
    
    for i in range(len(words[0])):
        for idx in range(len(words)):
            tmp = ''.join(words[idx][:i] + words[idx][i+1:])
            for word in words[idx:]:
                if( words[idx]!=word and tmp == ''.join(word[:i] + word[i+1:])):
                    dict_[word].append(words[idx])
                    dict_[words[idx]].append(word)
    stack = [begin]
    ans_dict[begin] = 0
    
    while(stack):
        now = stack.pop()
        num = ans_dict[now]
        for key in dict_[now]:
            if(ans_dict[key] > num):
                ans_dict[key] = num+1
                stack.append(key)
        
    answer = ans_dict[target]
    if(answer == 999999999):
        answer = 0
    
    return answer
