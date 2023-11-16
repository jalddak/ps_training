l = input().split("-")

num_list = []
for s in l:
    num = 0
    for n in s.split("+"):
        n = int(n)
        num += n
    num_list.append(num)

result = sum(num_list) - 2 * num_list[0]

print(-result)