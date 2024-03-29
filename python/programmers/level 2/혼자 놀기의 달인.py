def solution(cards):
    answer = 0
    visited = [True] + [False for _ in range(len(cards))]
    cards = [0] + cards
    groups = []
    for i in range(len(cards)):
        if visited[i]:
            continue
        visited[i] = True
        num = cards[i]
        cnt = 1
        while not visited[num]:
            cnt += 1
            visited[num] = True
            num = cards[num]
        groups.append(cnt)
    
    groups.sort(reverse=True)
    if len(groups) == 1:
        return 0
    answer = groups[0] * groups[1]
    return answer