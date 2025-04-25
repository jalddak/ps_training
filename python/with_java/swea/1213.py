answer = []

for _ in range(1, 11):
    tc = int(input())
    sb = "#" + str(tc) + " "
    x = input()
    string = input()
    cnt = 0

    for i in range(len(string) - len(x) + 1):
        flag = True
        for j in range(len(x)):
            if string[i+j] != x[j]:
                flag = False
                break
        if flag:
            cnt += 1
    
    sb += str(cnt)
    answer.append(sb)

for a in answer:
    print(a)