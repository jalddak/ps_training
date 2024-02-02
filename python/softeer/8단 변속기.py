import sys

DCT = list(map(int, input().split()))

answer = ["mixed", "ascending", "descending"]
result = 0
if DCT[0] == 8:
    result = -1
if DCT[0] == 1:
    result = 1

for i in range(1, 8):
    if DCT[i-1] < DCT[i] and result == 1:
        continue
    if DCT[i-1] > DCT[i] and result == -1:
        continue
    result = 0
    break

print(answer[result])