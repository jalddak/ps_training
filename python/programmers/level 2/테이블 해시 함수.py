def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    nums = []
    for i in range(row_begin, row_end+1):
        result = 0
        for n in data[i-1]:
            result += n % i
        nums.append(result)
    
    answer = nums[0]
    for i in range(1, len(nums)):
        answer = answer ^ nums[i]
    return answer