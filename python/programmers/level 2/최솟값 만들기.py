def solution(A,B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort(reverse=True)
    for i in range(length):
        answer += A[i] * B[i]

    return answer