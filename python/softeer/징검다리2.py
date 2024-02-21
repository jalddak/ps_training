import sys
input = sys.stdin.readline

N = int(input())
dols = list(map(int, input().split()))
r_dols = list(reversed(dols))

dp = [dols[0]]
rdp = [r_dols[0]]

cnt = [1]
rcnt = [1]

def bs(sorted_list, num):
    l, r = 0, len(sorted_list)
    while l <= r:
        mid = (l+r) // 2
        if sorted_list[mid] <= num:
            l = mid + 1
        else:
            r = mid - 1

    sorted_list[l] = num
        
        
def calc_cnt(dols, dp, cnt):
    global N
    for i in range(1, N):
        if dp[-1] < dols[i]:
            dp.append(dols[i])
        else:
            bs(dp, dols[i])
        
        cnt.append(len(dp))

calc_cnt(dols, dp, cnt)
calc_cnt(r_dols, rdp, rcnt)

rcnt.reverse()
print(max([cnt[i]+rcnt[i]-1 for i in range(N)]))
    
