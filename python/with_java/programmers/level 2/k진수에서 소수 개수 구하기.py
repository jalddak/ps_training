def make_candidate(n, k):
    nums = []
    while n != 0:
        nums.append(n % k)
        n = n // k
    nums.reverse()
    result = "".join(map(str, nums))
    result = result.split("0")
    return result

def check_prime(num):
    result = True
    for n in range(2, (int)(num ** 0.5)+1):
        if num % n == 0:
            result = False
            break
    return result

def solution(n, k):
    nums = make_candidate(n, k)
    answer = 0
    for num in nums:
        if len(num) == 0:
            continue
        num = int(num)
        if num <= 1:
            continue
        if check_prime(num):
            answer += 1
            
    return answer