import sys

answer = 0
for _ in range(5):
    s, e = input().split()
    sh, sm = map(int, s.split(':'))
    eh, em = map(int, e.split(':'))

    h = eh - sh
    m = em - sm

    answer += 60*h + m

print(answer)