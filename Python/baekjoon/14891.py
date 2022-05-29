from collections import deque

def turn(gears, index, direction, side):
    gear_copy = list(gears[index])[:]
    if direction == 1:
        back = gears[index].pop()
        gears[index].appendleft(back)
    elif direction == -1:
        front = gears[index].popleft()
        gears[index].append(front)

    if side == 2:
        if index != 4:
            if gear_copy[2] != gears[index+1][6]:
                turn(gears, index+1, -direction, 2)
    elif side == 1:
        if index != 1:
            if gear_copy[6] != gears[index-1][2]:
                turn(gears, index-1, -direction, 1)
    elif side == 0:
        if index != 4:
            if gear_copy[2] != gears[index+1][6]:
                turn(gears, index+1, -direction, 2)
        if index != 1:
            if gear_copy[6] != gears[index-1][2]:
                turn(gears, index-1, -direction, 1)


def main():
    gears = [[]]
    for i in range(4):
        gear = input()
        gear = deque([int(g) for g in gear])
        gears.append(gear)
    N = int(input())
    for i in range(N):
        index, direction = map(int, input().split())
        turn(gears, index, direction, 0)
        
    score = 0
    if gears[1][0] == 1:
        score += 1
    if gears[2][0] == 1:
        score += 2
    if gears[3][0] == 1:
        score += 4
    if gears[4][0] == 1:
        score += 8
    print(score)
    return score
    

if __name__ == '__main__':
    main()