def solution(food):
    half = []
    for i in range(1, len(food)):
        n = food[i] // 2
        for _ in range(n):
            half.append(i)
    reversed_half = list(reversed(half))
    answer = "".join(map(str, half + [0] + reversed_half))
    return answer