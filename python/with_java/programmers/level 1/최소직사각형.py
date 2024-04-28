def solution(sizes):
    sorted_sizes = list(map(sorted, sizes))
    answer = max(map(lambda x:x[1], sorted_sizes)) * max(map(lambda x:x[0], sorted_sizes))

    return answer