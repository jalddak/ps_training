# 문제를 통해 배운 점: 리스트의 요소를 한번에 str -> int 로 변환시키는 방법

def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    viewer = input().split()
    viewer = list(map(int, viewer))
    result = 0
    for i in range(len(A)):
        sub_check = A[i] - viewer[0]
        if sub_check <= 0:
            result += 1
        else:
            result += (sub_check // viewer[1]) + 1
            if sub_check % viewer[1] != 0:
                result += 1
    print(result)
    return result


if __name__ == '__main__':
    main()