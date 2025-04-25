answer = []

for t in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        checked = buildings[i-2:i+3]
        checked.sort(reverse=True)
        if buildings[i] == checked[0]:
            result += buildings[i] - checked[1]
    answer.append("#" + str(t) + " " + str(result))

for a in answer:
    print(a)
