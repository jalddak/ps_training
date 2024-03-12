def calc_gcd(a, b):
    if b == 0:
        return a
    return calc_gcd(b, a%b)

def check(gcd, array):
    for i in range(len(array)):
        if gcd == calc_gcd(gcd, array[i]):
            gcd = 0
            break
    return gcd

def solution(arrayA, arrayB):
    answer = 0
    length = len(arrayA)
    if length == 1:
        if arrayA[0] == arrayB[0]:
            return 0
        return max(arrayA[0], arrayB[0])

    A_gcd = arrayA[0]
    B_gcd = arrayB[0]
    for i in range(1, length):
        A_gcd = calc_gcd(A_gcd, arrayA[i])
        B_gcd = calc_gcd(B_gcd, arrayB[i])
        
    A_gcd = check(A_gcd, arrayB)
    B_gcd = check(B_gcd, arrayA)
    
    answer = max(A_gcd, B_gcd)
    
    return answer