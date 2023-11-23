from collections import deque

T = int(input())

for _ in range(T):
    command = input()
    n = int(input())
    inputNums = input()[1:-1].split(",")
    nums = []
    if inputNums[0].isdigit():
        nums = deque(map(int, inputNums))
    direction = 1
    flag = True
    for c in command:
        if c == "R":
            direction = -direction
        if c == "D":
            if len(nums) == 0:
                flag = False
                break
            if direction == 1:
                nums.popleft()
            elif direction == -1:
                nums.pop()
    if not flag:
        print("error")
    else:
        if direction == -1:
            nums.reverse()
        print("[", end="")
        nums = map(str, nums)
        nums = ",".join(nums)
        print(nums, end="")
        print("]")
