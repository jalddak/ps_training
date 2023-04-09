def solution(money):
    answer = 0
    if len(money) == 3:
        return max(money)
    # 마지막 제외
    not_last = money[:-1]
    nl_most = [not_last[0], not_last[1], not_last[0] + not_last[2]]
    for i in range(3, len(not_last)):
        most = not_last[i] + max(nl_most[i-3], nl_most[i-2])
        nl_most.append(most)
    # 첫째 제외
    not_first = money[1:]
    nf_most = [not_first[0], not_first[1], not_first[0] + not_first[2]]
    for i in range(3, len(not_first)):
        most = not_first[i] + max(nf_most[i-3], nf_most[i-2])
        nf_most.append(most)
    
    answer = max(max(nl_most), max(nf_most))
    return answer