N = int(input())
minus = []
plus = []

for _ in range(N):
    num = int(input())
    if num <= 0:
        minus.append(num)
    else:
        plus.append(num)

minus.sort()
plus.sort(reverse=True)

def calc_max(l):
    result = 0
    i = 0
    while i < len(l):
        if i == len(l)-1 or l[i]*l[i+1] < l[i]+l[i+1]:
            result += l[i]
            i += 1
            continue
        result += l[i]*l[i+1]
        i += 2
    return result

mzsum = calc_max(minus)
psum = calc_max(plus)

print(mzsum + psum)
