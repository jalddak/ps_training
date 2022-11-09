a, b = map(int, input().strip().split(' '))

star = ''
for _ in range(a):
    star += '*'

for _ in range(b):
    print(star)
        