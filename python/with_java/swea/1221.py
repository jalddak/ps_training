stoi = {"ZRO":0, 
        "ONE":1, 
        "TWO":2,
        "THR":3,
        "FOR":4,
        "FIV":5,
        "SIX":6,
        "SVN":7,
        "EGT":8,
        "NIN":9}

itos = {0:"ZRO", 
        1:"ONE", 
        2:"TWO",
        3:"THR",
        4:"FOR",
        5:"FIV",
        6:"SIX",
        7:"SVN",
        8:"EGT",
        9:"NIN"}

tcCnt = int(input())

answer = []
for _ in range(tcCnt):
    pre, length = input().split()
    s = input().split()
    nums = []
    for snum in s:
        nums.append(stoi[snum])
    nums.sort()
    result = []
    for num in nums:
        result.append(itos[num])

    sb = pre + " " + " ".join(result)
    answer.append(sb)

print("\n".join(answer))
