def calc(N, numbers, operator, order):
    candidates = []
    for i in range(4):
        operator_copy = operator[:]
        order_copy = order[:]
        if operator[i] == 0:
            continue
        operator_copy[i] -= 1
        order_copy.append(i)
        candidates.append(calc(N, numbers, operator_copy, order_copy))
    if len(candidates) == 0:
        result = numbers[0]
        for i in range(N-1):
            if order[i] == 0:
                result += numbers[i+1]
            elif order[i] == 1:
                result -= numbers[i+1]
            elif order[i] == 2:
                result *= numbers[i+1]
            elif order[i] == 3:
                if result < 0:
                    result = -result
                    result = -(result // numbers[i+1])
                else:
                    result = result // numbers[i+1]
        return result
    # 새로 알게 된 것
    elif type(candidates[0]) is int:
        maximum = max(candidates)
        minimum = min(candidates)
    else:
        # 새로 알게 된 것
        candidates_max = [c[0] for c in candidates]
        candidates_min = [c[1] for c in candidates]
        maximum = max(candidates_max)
        minimum = min(candidates_min)
    return maximum, minimum
        


def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    maximum, minimum = calc(N, numbers, operator, [])
    print(maximum)
    print(minimum)



if __name__ == '__main__':
    main()