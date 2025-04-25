n = int(input())

def recursion(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    half = n // 2
    result = recursion(half)
    for i in range(half):
        result.append(result[i] + " " + result[i])
        result[i] = " " * half + result[i] + " " * half

    return result


for r in recursion(n):
    print(r)