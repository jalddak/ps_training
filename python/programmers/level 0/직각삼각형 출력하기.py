n = int(input())
for i in range(n):
    star = ''
    for _ in range(i+1):
        star += '*'
    print(star)