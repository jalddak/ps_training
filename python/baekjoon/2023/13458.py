global n, a, b, c, result

n = int(input())
a = list(map(int, input().split()))

temp = list(map(int, input().split()))
b = temp[0]
c = temp[1]

result = 0

def main():
    global n, a, b, c, result
    for i in range(n):
        a[i] -= b
        result += 1
        if a[i] > 0:
            result += a[i] // c
            if a[i] % c > 0:
                result += 1

    return -1

if __name__ == '__main__':
    main()
    print(result)