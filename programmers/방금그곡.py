import re
def solution(m, musicinfos):
    answer = ''
    
    musicinfos = list(map(lambda x:x.split(',') , musicinfos))
    pat = re.compile('[A-Z]{1}#{0,1}')
    now_ = ['',0]
    m = pat.findall(m)
    
    for st,en,name,um in musicinfos:
        # en - st
        st = st.split(':')
        en = en.split(':')
        
        st = int(st[0]) * 60 + int(st[1])
        en = int(en[0]) * 60 + int(en[1])
        um = pat.findall(um)
        
        dif = en - st
        
        um = um * (dif // (len(um)) + 1)
        um = um[:dif]
        cnt = 0
        
        for i in range(0,len(um)-len(m)+1):
            if(um[i:i+len(m)] == m):
                if(now_[1] < len(um)):
                    now_ = [name,len(um)]
                break
        
#        for i in um:
#            if(m[cnt] == i):
#                cnt += 1
#            else:
#                cnt = 0
#            if(cnt == len(m)):
#                if( now_[1] < len(um) ):
#                    now_ = [name,len(um)]
#                break
    answer = now_[0]
    if(now_[1] == 0):
        answer = '(None)'
    return answer
