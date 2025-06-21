def recursion(a, b, c):
    if b == 1:
        return a % c
    temp = recursion(a, b // 2, c)
    if b % 2 == 1:
        return temp * temp * a % c
    else:
        return temp * temp % c
    
def main():
    a, b, c = map(int, input().split())
    print(recursion(a, b, c))

if __name__ == "__main__":
    main()