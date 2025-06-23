def rc(n):
    result = []
    if n == 3:
        result.append("  *  ")
        result.append(" * * ")
        result.append("*****")
        return result
    nn = n // 2
    before = rc(nn)

    for row in before:
        result.append(" " * nn + row + " " * nn)

    for row in before:
        result.append(row + " " + row)
    
    return result

def main():
    n = int(input())
    answer = rc(n)
    for row in answer:
        print(row)


if __name__ == "__main__":
    main()