global n, schedule, visited, result

n = int(input())
schedule = []
ables = [0 for _ in range(n+1)]
for _ in range(n):
    schedule.append(list(map(int, input().split())))
result = 0

def main():
    global n, schedule, ables, result
    for i in range(n):
        if i > 0 and ables[i] < ables[i-1]:
            ables[i] = ables[i-1]
        if i + schedule[i][0] < n + 1:
            ables[i + schedule[i][0]] = max(ables[i + schedule[i][0]], ables[i] + schedule[i][1])

if __name__ == '__main__':
    main()
    print(max(ables))