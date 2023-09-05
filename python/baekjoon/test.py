arr = [4, 1, 2, 3]

check = [0 for _ in range(len(arr))]

print(check)

for n in arr:
    if check[n-1] == 0:
        check[n-1] += 1
    else:
        break

print(check)