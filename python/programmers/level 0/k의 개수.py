def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        for letter in str(num):
            if int(letter) == k:
                answer += 1
    return answer