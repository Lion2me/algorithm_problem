import re
from itertools import permutations
from copy import deepcopy
def minus(nums,opers):
    try:
        while(True):
            idx = opers.index('-')
            nums[idx] -= nums[idx+1]
            nums = nums[:idx+1] + nums[idx+2:]
            opers = opers[:idx] + opers[idx+1:]
    except:
        return nums, opers
    
def plus(nums,opers):
    try:
        while(True):
            idx = opers.index('+')
            nums[idx] += nums[idx+1]
            nums = nums[:idx+1] + nums[idx+2:]
            opers = opers[:idx] + opers[idx+1:]
    except:
        return nums, opers
def gob(nums,opers):
    try:
        while(True):
            idx = opers.index('*')
            nums[idx] *= nums[idx+1]
            nums = nums[:idx+1] + nums[idx+2:]
            opers = opers[:idx] + opers[idx+1:]
    except:
        return nums, opers
def solution(expression):
    
    answer = 0
    
    nums = re.findall('[0-9]+',expression)
    opers = re.findall('[^0-9]+',expression)
    nums = list(map(lambda x:int(x) , nums))
    
    tmp = '+-*'
    max_ = 0
    for reg in list(permutations(tmp)):
        nums_tmp = deepcopy(nums)
        opers_tmp = deepcopy(opers)
        for i in reg:
            if(i == '+'):
                nums_tmp , opers_tmp = plus(nums_tmp,opers_tmp)
            elif(i == '*'):
                nums_tmp , opers_tmp = gob(nums_tmp,opers_tmp)
            elif(i == '-'):
                nums_tmp , opers_tmp = minus(nums_tmp,opers_tmp)
        if(abs(nums_tmp[0]) > max_):
            max_ = abs(nums_tmp[0])
    answer = max_
    return answer
