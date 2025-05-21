num = input()

cnts = [0 for _ in range(10)]
for n in num:
    cnts[int(n)] += 1

sn = cnts[6] + cnts[9]
cnts[6] = 0
cnts[9] = 0

sn = sn // 2 + (1 if sn % 2 != 0 else 0)
answer = max(sn, max(cnts))
print(answer)