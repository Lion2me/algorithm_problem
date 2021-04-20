import re
from collections import Counter , defaultdict
def solution(str1, str2):
    answer = 0
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    str1_tmp = []
    str2_tmp = []
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if(len(re.findall('[^A-Z]',tmp)) > 0):
            continue
        str1_tmp.append(tmp)
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if(len(re.findall('[^A-Z]',tmp)) > 0):
            continue
        str2_tmp.append(tmp)
        
    dict_1 = defaultdict(int,Counter(str1_tmp))
    dict_2 = defaultdict(int,Counter(str2_tmp))
    min_dict = defaultdict(int)
    max_dict = defaultdict(int)
    keys = list(set(list(dict_1.keys()) + list(dict_2.keys())))
    
    for i in keys:
        min_dict[i] = min(dict_1[i], dict_2[i])
        max_dict[i] = max(dict_1[i], dict_2[i])
    if(len(max_dict.keys()) == 0):
        return 1*65536
        
    answer = int(sum(min_dict.values()) / sum(max_dict.values()) * 65536)
    
    return answer
