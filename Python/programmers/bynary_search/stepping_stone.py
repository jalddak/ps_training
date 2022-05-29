def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    max_distance = 1000000000
    min_distance = 1
    while min_distance <= max_distance:
        mid_distance = (max_distance + min_distance) // 2
        i = 0
        count = 0
        test_rocks = rocks[:]
        while i < len(test_rocks) + 1:
            between = 0
            if len(test_rocks) == 0:
                between = distance
            elif i == 0:
                between = test_rocks[i]
            elif i == len(test_rocks):
                between = distance - test_rocks[i-1]
            else:
                between = test_rocks[i]-test_rocks[i-1]
            print(mid_distance, between, i, count, test_rocks)
            if between < mid_distance:
                count += 1
                if count > n:
                    break
                test_rocks.pop(i)
                i -= 1
            i += 1
        if count > n:
            max_distance = mid_distance - 1
        elif count <= n:
            answer = mid_distance
            min_distance = mid_distance + 1
        print(max_distance, min_distance, mid_distance, answer)
    return answer

solution(23, [3, 6, 9, 10, 14, 18], 2)