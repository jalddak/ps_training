n = int(input())

def rc(l):
    if l == 1:
        return "*"

    nl = l // 3
    frag = rc(nl)
    result = []
    for row in frag:
        result.append(row * 3)
    for row in frag:
        result.append(row + " " * nl + row)
    for row in frag:
        result.append(row * 3)
    return result

def main():
    for row in rc(n):
        print(row)

if __name__ == "__main__":
    main()
