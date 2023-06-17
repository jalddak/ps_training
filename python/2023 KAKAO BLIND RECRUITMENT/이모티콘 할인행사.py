def match(users, depth, prices, rates):
    # emoticon plus user num, total sales
    epun, ts = [0, 0]
    
    for user in users:
        price = 0
        for i in range(depth):
            if user[0] <= rates[i]:
                price += prices[i]
        if price >= user[1]:
            epun += 1
        else:
            ts += price
    
    return [epun, ts]


def dfs(users, depth, prices, rates):
    if depth == len(prices):
        return match(users, depth, prices, rates)
    
    discount = [40, 30, 20, 10]
    
    candidates = []
    for d in discount:
        new_prices = prices[:]
        new_rates = rates[:]
        new_rates.append(d)
        new_prices[depth] /= 100
        new_prices[depth] = int(new_prices[depth]) * (100-d)
        candidates.append(dfs(users, depth+1, new_prices, new_rates))
    
    candidates.sort(key = lambda x:(-x[0], -x[1]))
    return candidates[0]

        
def solution(users, emoticons):
    prices = emoticons[:]
    return dfs(users, 0, prices, [])


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))