N = int(input())
nums = list(map(int, input().split()))
nums.sort()

near_zero = 1000000000 * 3
answer = []

for i in range(N-2):
    select = nums[i]
    s, e = i+1, N-1
    while s < e:
        total = select + nums[s] + nums[e]
        if abs(total) < near_zero:
            near_zero = abs(total)
            answer = [select, nums[s], nums[e]]
        if total < 0:
            s += 1
        elif total > 0:
            e -= 1
        else:
            print(select, nums[s], nums[e])
            exit()
print(" ".join(map(str, answer)))
    

# N = int(input())
# nums = list(map(int, input().split()))
# nums.sort()

# def bs(temp, n):
#     s, e = 0, len(temp)-1
#     result = s if abs(temp[s]-n) < abs(temp[e]-n) else e

#     while s <= e:
#         m = (s+e) // 2
#         if temp[m] < n:
#             result = m if abs(temp[m]-n) < abs(temp[result]-n) else result
#             s = m + 1
#         elif temp[m] > n:
#             result = m if abs(temp[m]-n) < abs(temp[result]-n) else result
#             e = m - 1
#         else:
#             return m
#     return result

# left = 0
# right = N-1
# answer = []
# zero_mix = 0

# for left in range(N-2):
#     for right in range(left+2, N):
#         mix = nums[left] + nums[right]
#         temp = nums[left+1:right]
#         mid = bs(temp, -mix)
#         mix += temp[mid]
#         if not answer or abs(mix) < zero_mix:
#             answer = [nums[left], temp[mid], nums[right]]
#             zero_mix = abs(mix)
#             if zero_mix == 0:
#                 print(" ".join(map(str, answer)))
#                 exit()
# print(" ".join(map(str, answer)))