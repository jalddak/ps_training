import sys

input = sys.stdin.readline

N, M = map(int, input().split())
names = []
available = {}
for _ in range(N):
    name = input()[:-1]
    names.append(name)
    available[name] = available.get(name, [True for _ in range(10)])
    available[name][-1] = False
names.sort()

for _ in range(M):
    name, start, end = input().split()
    start, end = map(lambda x:x-9, map(int, [start, end]))
    for i in range(start, end):
        available[name][i] = False

for name in names:
    print("Room " + name + ":")
    times = available[name]
    if set(times) == {False}:
        print("Not available")
    else:
        start = -1
        end = -1
        ats = []
        for i in range(10):
            if times[i] and start == -1:
                start = i
            elif not times[i] and start != -1:
                end = i
                start, end = map(str, map(lambda x:x+9, [start, end]))
                start = start if len(start) == 2 else "0" + start
                end = end if len(end) == 2 else "0" + end
                ats.append(start + "-" + end)
                start = -1
        print(str(len(ats)) + " available:")
        for t in ats:
            print(t)
        
    if name != names[-1]:
        print("-----")
    