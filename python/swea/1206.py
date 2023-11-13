for i in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for j in range(2, n - 1):
        range_building = building[j-2:j+3]
        range_building.sort(reverse=True)
        if building[j] == range_building[0]:
            result += building[j] - range_building[1]
    print("#" + str(i) + " " + str(result))