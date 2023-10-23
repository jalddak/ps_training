i = 1
flag = 0
for n in list(map(int, input().split())):
    if n == i and flag != -1:
        flag = 1
    elif n == 9 - i and flag != 1:
        flag = -1
    else:
        print("mixed")
        exit()
    i += 1

if flag == 1:
    print("ascending")
else:
    print("descending")