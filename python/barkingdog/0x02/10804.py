cards = [n for n in range(1, 21)]

for _ in range(10):
    a, b = map(lambda x:x-1, map(int, input().split()))
    
    while a < b:
        temp = cards[a]
        cards[a] = cards[b]
        cards[b] = temp
        a += 1
        b -= 1

print(*cards)