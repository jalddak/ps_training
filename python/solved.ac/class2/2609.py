n1, n2 = map(int, input().split())

l1 = []
l2 = []
def calc(n, l):
    for i in range(1, int(n**0.5) + 1):
        if i not in l and n%i == 0:
            l.append(i)
            if i != n //i:
                l.append(n//i)

calc(n1, l1)
calc(n2, l2)
l1.sort()
l2.sort()

r1 = 0
for n in l1:
    if n in l2:
        r1 = n

r2 = r1 * (n1//r1) * (n2//r1)

print(r1)
print(r2)