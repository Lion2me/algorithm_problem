def solution(brown, yellow):
    answer = []
    # 사각형을 만들 수 있는 조건
    
    # brown + yellow = return을 곱한거
    # (brown + 4) /2 = return[0]  + return[1]
    garo = int(brown/2)
    sero = 2
    while(True):
        if(garo + sero == int((brown+4)/2) and garo * sero == brown + yellow):
            break
        else:
            garo -= 1
            sero += 1
    answer = [garo,sero]
    
    return answer
