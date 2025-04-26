a = "| 1 2 3 4 | 5 6 7 8 | 9 10 11 12"

t = list(a.split("| "))

result = []
for b in t:
    result.append(list(map(int, b.split())))

print(result)