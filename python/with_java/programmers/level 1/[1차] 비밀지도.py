def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        b1 = list(reversed(list(bin(arr1[i])[2:])))
        b2 = list(reversed(list(bin(arr2[i])[2:])))
        for _ in range(n-len(b1)):
            b1.append("0")
        for _ in range(n-len(b2)):
            b2.append("0")
        b1.reverse()
        b2.reverse()
        row = []
        for i in range(n):
            if b1[i] == "1" or b2[i] == "1":
                row.append("#")
            else:
                row.append(" ")
        answer.append("".join(row))
    
    return answer