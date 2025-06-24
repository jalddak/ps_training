n = int(input())
answer = 0
loca = [-1 for _ in range(n)]

def back(depth):
    global n, answer

    if depth == n:
        answer += 1
        return
    
    for i in range(n):
        flag = True
        for j in range(depth):
            if loca[j] == i or abs(loca[j] - i) == abs(j - depth):
                flag = False
                break
        if not flag:
            continue
        loca[depth] = i
        back(depth + 1)

def main():
    global answer

    back(0)

    print(answer)

if __name__ == "__main__":
    main()