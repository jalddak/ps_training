n = int(input())

d = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age not in d:
        d[age] = [name]
    else:
        d[age].append(name)

for age in sorted(list(d.keys())):
    for name in d[age]:
        print(age, name)