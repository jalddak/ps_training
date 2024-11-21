cmd = input()

minus = cmd.split("-")

answer = sum(map(int, minus[0].split("+")))
for i in range(1, len(minus)):
    answer -= sum(map(int, minus[i].split("+")))

print(answer)