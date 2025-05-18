# 16 ~ 20 테스트에서 다 시간초과남
# 게속 수정한 코드인데 여기까지가 한계임
# 질문 게시판에 개쉬운코드 쳐봐버려서 이미 이문제는 평생 틀린문제임
# 기억속에서 삭제될때나 다시 봐야할듯
# 그냥 개빡침

def solution(cap, n, deliveries, pickups):
    answer = 0
    d = []
    p = []
    for i in range(n):
        if deliveries[i] != 0:
            d.append(i)
        if pickups[i] != 0:
            p.append(i)
            
    while len(d) > 0 or len(p) > 0:
        max_d, max_p = [0, 0]
        if len(d) > 0:
            max_d = max(d)
        if len(p) > 0:
            max_p = max(p)
        ep = max(max_d, max_p)
        d_cap = 0
        p_cap = 0
        answer += 2*(ep+1)
        while len(d) > 0 and d_cap < cap:
            d_i = d.pop()
            while d_cap < cap and deliveries[d_i] > 0:
                deliveries[d_i] -= 1
                d_cap += 1
            if deliveries[d_i] > 0:
                d.append(d_i)
        while len(p) > 0 and p_cap < cap:
            p_i = p.pop()
            while p_cap < cap and pickups[p_i] > 0:
                pickups[p_i] -= 1
                p_cap += 1
            if pickups[p_i] > 0:
                p.append(p_i)
                
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)