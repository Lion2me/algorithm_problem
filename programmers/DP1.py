board = [10 for i in range(32005)]
N_ = 0
tmp = 0
def check_num(prev,count,now_num):
    global board , N_
    if( now_num <= 0 or now_num > 32000 or count > 8):
        return
    elif(board[now_num] > count):
        board[now_num] = count
        
    elif(board[now_num] <= count):
        return
    if count == 1:
        for i in range(1,9-count):
            check_num(now_num,count+i,int(str(now_num)+str(N_)*i))
            
    for idx in range(1,9-count):
        
        check_num(now_num,count+idx+1,now_num * int('1'*idx) )
        check_num(now_num,count+idx+1,now_num + int('1'*idx) )
        check_num(now_num,count+idx+1,now_num - int('1'*idx) )
        check_num(now_num,count+idx+1,int(now_num / int('1'*idx) ))

        
        check_num(now_num,count+idx,now_num * int(str(N_)*idx) )
        check_num(now_num,count+idx,now_num + int(str(N_)*idx) )
        
        check_num(now_num,count+idx,now_num - int(str(N_)*idx) )
        check_num(now_num,count+idx,int(str(N_)*idx) - now_num)
        
        check_num(now_num,count+idx,int(int(str(N_)*idx) / now_num))
        check_num(now_num,count+idx,int(now_num / int(str(N_)*idx)))
        
def solution(N, number):
    answer = 0
    
    global board, N_ , tmp
    
    N_ = N
    tmp = number
    
    check_num(0,1,N)
    if(board[number] > 8):
        answer = -1
    else:
        answer = board[number]
    return answer
