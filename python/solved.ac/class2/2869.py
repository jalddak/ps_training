a, b, v = map(int, input().split())

result = (v-a) // (a-b) + 1
result += 1 if (v-a) % (a-b) != 0 else 0

print(result)