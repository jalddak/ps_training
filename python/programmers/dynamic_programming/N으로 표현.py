# 이전에 내가 푼 코드는 무슨소리하는 지 모르겠고, 어떻게 푸는지 몰라서 어떤 방식이 이용되었는지만 찾아봤다.
# 동적계획법의 가장 핵심이 반복되는 그 방법을 찾는 점화식을 구하는것이라고 생각하는데 난 그게 너무 약하다.
# 결론 : 큰일이다.

def solution(N, number):
    answer = 0
    candidates = []
    while answer < 9:
        answer += 1
        calc(N, answer, candidates)
        
        if number in candidates[answer-1]:
            return answer
        
    return -1

def calc(N, cnt, candidates):
    if cnt == 1:
        candidates.append([N])
    elif cnt == 2:
        candidates.append([N+N, N-N, N*N, int(N/N), N*11])
    if cnt >= 3:
        result = []
        for n in range(1, cnt):
            first = candidates[n-1]
            second = candidates[cnt-n-1]
            for i in range(len(first)):
                for j in range(len(second)): 
                    plus = first[i] + second[j]
                    minus = first[i] - second[j]
                    mult = first[i] * second[j]
                    if second[j] != 0:
                        div = first[i] // second[j]
                        result.append(int(div))
                    result.append(int(plus))
                    result.append(int(minus))
                    result.append(int(mult))
        num = ''
        for _ in range(cnt):
            num += str(N)
        result.append(int(num))
        result = list(set(result))
        candidates.append(result)