from itertools import permutations

def sosu(x):
    if(x == 1 or x == 0):
        return False
    for i in range(2,int(x/2)+1):
        if( x % i == 0):
            return False
    return True

def solution(numbers):
    answer = 0
    set_ = set()
    for i in range(1,len(numbers)+1):
        tmp = list(permutations(numbers,i))
        for num in tmp:
            number = int(''.join(num))
            if(sosu(number) == True):
                set_.add(number)
    answer = len(set_)
    return answer
