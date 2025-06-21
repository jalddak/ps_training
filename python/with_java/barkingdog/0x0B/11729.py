cnt = 0
answer = []

def rc(a, b, n):
    global cnt, answer
    if n == 0:
        return
    cnt += 1
    rc(a, 6-a-b, n-1)
    answer.append(str(a) + " " + str(b))
    rc(6-a-b, b, n-1)

def main():
    global cnt, answer
    n = int(input())
    rc(1, 3, n)
    print(cnt)
    print("\n".join(answer))

if __name__ == "__main__":
    main()