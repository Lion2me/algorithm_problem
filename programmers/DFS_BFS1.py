nums = []
goal = 0
tmp = 0

def solve(idx,now_sum):
    global tmp,nums,goal
    if(idx == len(nums)):
        if(now_sum == goal):
            tmp += 1
        return
    else:
        solve(idx+1,now_sum-nums[idx])
        solve(idx+1,now_sum+nums[idx])

def solution(numbers, target):
    
    dict_ = {}
    
    global nums,goal,tmp
    nums = numbers
    goal = target
    
    solve(0,0)
    
    answer = tmp
    return answer
