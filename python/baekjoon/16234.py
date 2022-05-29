def move(N, L, R, land):
    union_list = []
    for i in range(N):
        for j in range(N):
            union = [(i,j)]
            if j != N-1:
                comp_right = abs(land[i][j] - land[i][j+1])
                if comp_right >= L and comp_right <= R:
                    union.append((i,j+1))
            if i != N-1:
                comp_down = abs(land[i][j] - land[i+1][j])
                if comp_down >= L and comp_down <= R:
                    union.append((i+1,j))
            union = set(union)
            if len(union) > 1:
                index = 0
                pos_index = []
                while index < len(union_list):
                    if union_list[index].intersection(union) != set():
                        pos_index.append(index)
                    index += 1
                if len(pos_index) > 0:
                    pos_index.sort(reverse = True)
                    min_index = pos_index.pop()
                    for index in pos_index:
                        union_list[min_index] = union_list[min_index].union(union_list[index])
                        union_list.pop(index)
                    union_list[min_index] = union_list[min_index].union(union)

                if index == len(union_list):
                    union_list.append(union)
    if len(union_list) == 0:
        return 0
    else:
        union_list = list(map(list, union_list))
        for i in range(len(union_list)):
            sum = 0
            for j in range(len(union_list[i])):
                sum += land[union_list[i][j][0]][union_list[i][j][1]]
            average = sum // len(union_list[i])
            for j in range(len(union_list[i])):
                land[union_list[i][j][0]][union_list[i][j][1]] = average
        return land

def main():
    N, L, R = map(int, input().split())
    land = []
    for _ in range(N):
        land.append(list(map(int, input().split())))

    move_count = 0
    while land != 0:
        land = move(N, L, R, land)
        move_count += 1
    move_count -= 1
    print(move_count)
    return(move_count)


if __name__ == '__main__':
    main()