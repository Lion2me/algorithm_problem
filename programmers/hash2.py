def solution(phone_book):
    
    dict_ = {}
    
    phone_book = sorted(phone_book,key = lambda x:len(x))
    
    answer = True
    
    for i in phone_book:
        for j in range(1,21):
            if i[:j] in dict_:
                answer = False
        dict_[i] = True
                
    return answer
