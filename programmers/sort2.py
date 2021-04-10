import itertools

def solution(numbers):
    if(sum(numbers) == 0):
        answer = '0'
    else:
        numbers = [str(num) for num in numbers]
        numbers_tmp = []
        for i in range(len(numbers)):
            tmp_string = numbers[i]*5
            numbers_tmp.append( ( tmp_string[:4] , numbers[i] ) )

        numbers_tmp = sorted(numbers_tmp, key = lambda x:x[0])[::-1]
        answer = ''.join(list(map(lambda x:x[1],numbers_tmp)))
    
    return answer
