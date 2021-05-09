from collections import defaultdict

dict_price = defaultdict(int)
dict_graph = defaultdict(str)
def pay_dfs(user,price):
    if(user == ''):
        return
    send = int(price/10)
    dict_price[user] += (price-send)
    pay_dfs(dict_graph[user] , send)
    
def solution(enroll, referral, seller, amount):
    answer = []
    
    global dict_price , dict_graph
    dict_price['-'] = 0
    dict_graph['-'] = ''
    
    amount = list(map(lambda x:x*100,amount))
    
    for i in range(len(enroll)):
        dict_price[enroll[i]] = 0
        dict_graph[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        pay_dfs(seller[i],amount[i])
    
    for i in enroll:
        answer.append(dict_price[i])
    
    return answer
