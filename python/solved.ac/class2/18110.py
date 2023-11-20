import sys
input = sys.stdin.readline

n = int(input())

except_num = n * 0.15
if except_num - int(except_num) >= 0.5:
    except_num = int(except_num) + 1
else:
    except_num = int(except_num)

scores = [int(input()) for _ in range(n)]
scores.sort()

if except_num != 0:
    scores = scores[except_num:-except_num]

result = sum(scores) / len(scores) if sum(scores) != 0 else 0

result = int(result)+1 if result - int(result) >= 0.5 else int(result)

print(result)