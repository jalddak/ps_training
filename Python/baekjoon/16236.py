# 방향 탐색이라고 전에갔던 방향으로만 안가는것만 생각했는데
# 그냥 체크했던 부분을 기록하면서 가는게 맞게 푸는것이였다.

def bfs(space, fish, sec, temp_sec, shark_size, shark_location, shark_stack, already_check):
    if len(fish) == 0 or len(shark_location) == 0:
        return sec
    elif fish[0] >= shark_size:
        return sec
    
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    temp_sec += 1
    new_shark_location = []
    check = 0
    for l in range(len(shark_location)):
        for i in range(4):
            y = shark_location[l][0] + dy[i]
            x = shark_location[l][1] + dx[i]
            if (y,x) in already_check:
                continue
            already_check.append((y,x))
            if y >= 0 and y < len(space) and x >= 0 and x < len(space):
                direction = i - 2
                if direction < 0:
                    direction += 4
                if space[y][x] < shark_size and space[y][x] != 0 and space[y][x] != 9:
                    if check == 0:
                        new_shark_location = [(y,x)]
                        check = 1
                    else:
                        new_shark_location.append((y,x))
                elif space[y][x] == shark_size or space[y][x] == 0 or space[y][x] == 9:
                    if check == 0:
                        new_shark_location.append((y,x))
    if check == 1:
        sec = temp_sec
        new_shark_location = list(set(new_shark_location))
        new_shark_location = list(map(list, new_shark_location))
        new_shark_location.sort(key = lambda x : (-x[0], -x[1]))
        final_location = new_shark_location.pop()
        new_shark_location = [(final_location[0], final_location[1])]
        fish.remove(space[final_location[0]][final_location[1]])
        space[final_location[0]][final_location[1]] = 0
        shark_stack += 1
        if shark_stack == shark_size:
            shark_size += 1
            shark_stack = 0
        return bfs(space, fish, sec, temp_sec, shark_size, new_shark_location, shark_stack, [])
    return bfs(space, fish, sec, temp_sec, shark_size, new_shark_location, shark_stack, already_check)



def main():
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    fish = []
    shark_location = []
    for i in range(N):
        for j in range(N):
            if space[i][j] != 0 and space[i][j] != 9:
                fish.append(space[i][j])
            elif space[i][j] == 9:
                shark_location.append((i,j))
    fish.sort()
    sec = bfs(space, fish, 0, 0, 2, shark_location, 0, shark_location)
    print(sec)
    return sec

if __name__ == '__main__':
    main()