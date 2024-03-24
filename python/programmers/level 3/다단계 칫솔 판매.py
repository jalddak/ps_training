def solution(enroll, referral, seller, amount):
    answer = []
    info = {}
    n = len(enroll)
    for i in range(n):
        info[enroll[i]] = [referral[i], 0]
    m = len(seller)
    for i in range(m):
        name, cost = seller[i], amount[i] * 100
        while name != "-" and cost > 0:
            incentive = cost // 10
            info[name][1] += cost - incentive
            name = info[name][0]
            cost = incentive
    for name in enroll:
        answer.append(info[name][1])
    return answer