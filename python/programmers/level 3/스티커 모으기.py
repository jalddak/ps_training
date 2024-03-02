def dp_calc(sticker):
    dp = [sticker[0], max(sticker[0], sticker[1])]
    for i in range(2, len(sticker)):
        dp.append(max(dp[-1], dp[-2]+sticker[i]))
    return dp

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker)
    answer = 0
    sf = sticker[:-1]
    ss = sticker[1:]
    
    answer = max(dp_calc(sf)[-1], dp_calc(ss)[-1])
    return answer
    

    return answer