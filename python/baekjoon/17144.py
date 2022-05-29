def diffusion(room, R, C):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(R):
        for j in range(C):
            if room[i][j][0] > 0:
                dust = room[i][j][0] // 5
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if y >= 0 and y < R and x >= 0 and x < C:
                        if room[y][x][0] != -1:
                            if len(room[y][x]) == 1:
                                room[y][x].append(dust)
                            else:
                                room[y][x][1] += dust
                            room[i][j][0] -= dust
    for i in range(R):
        for j in range(C):
            if len(room[i][j]) == 2:
                room[i][j][0] += room[i][j].pop()


def clean(room, air_cleaner, R, C):
    up = 1
    for cleaner_location in air_cleaner:
        y = cleaner_location[0]
        x = cleaner_location[1]
        if up == 1:
            while y > 0:
                if cleaner_location[0] != y:
                    room[y][x][0] = room[y-1][x][0]
                y -= 1
            while x < C - 1:
                room[y][x][0] = room[y][x+1][0]
                x += 1
            while y < cleaner_location[0]:
                room[y][x][0] = room[y+1][x][0]
                y += 1
            while x > cleaner_location[1] + 1:
                room[y][x][0] = room[y][x-1][0]
                x -= 1
            room[y][x][0] = 0
            up = 0
        else:
            while y < R - 1:
                if cleaner_location[0] != y:
                    room[y][x][0] = room[y+1][x][0]
                y += 1
            while x < C - 1:
                room[y][x][0] = room[y][x+1][0]
                x += 1
            while y > cleaner_location[0]:
                room[y][x][0] = room[y-1][x][0]
                y -= 1
            while x > cleaner_location[1] + 1:
                room[y][x][0] = room[y][x-1][0]
                x -= 1
            room[y][x][0] = 0


def main():
    R, C, T = map(int, input().split())
    room = [[[] for _ in range(C)] for _ in range(R)]
    air_cleaner = []
    for i in range(R):
        room_row = list(map(int, input().split()))
        for j in range(C):
            room[i][j].append(room_row[j])
            if room_row[j] == -1:
                air_cleaner.append((i,j))
    
    for _ in range(T):
        diffusion(room, R, C)
        clean(room, air_cleaner, R, C)

    dust = 0
    for i in range(R):
        for j in range(C):
            if room[i][j][0] != -1:
                dust += room[i][j][0]
    print(dust)


if __name__ == '__main__':
    main()