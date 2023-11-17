T = int(input())

for C in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    stack = [num]
    for _ in range(cnt):
        n_stack = []
        while len(stack) != 0:
            num_temp = stack.pop()
            for i in range(len(num)):
                for j in range(i+1, len(num)):
                    num_list = list(num_temp)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    n_stack.append(''.join(num_list))
        stack = list(set(n_stack))
    print("#" + str(C) + " " + str(max(list(map(int, stack)))))