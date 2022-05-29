def rotate(face, direction):
    after = [['_' for _ in range(3)] for _ in range(3)]
    if direction == '-':
        after[1][1] = face[1][1]
        after[0][0] = face[0][2]
        after[0][1] = face[1][2]
        after[0][2] = face[2][2]
        after[1][2] = face[2][1]
        after[2][2] = face[2][0]
        after[2][1] = face[1][0]
        after[2][0] = face[0][0]
        after[1][0] = face[0][1]
    elif direction == '+':
        after[1][1] = face[1][1]
        after[0][2] = face[0][0]
        after[1][2] = face[0][1]
        after[2][2] = face[0][2]
        after[2][1] = face[1][2]
        after[2][0] = face[2][2]
        after[1][0] = face[2][1]
        after[0][0] = face[2][0]
        after[0][1] = face[1][0]
    return after


def main():
    n = int(input())
    for _ in range(n):
        up = [['w' for _ in range(3)] for _ in range(3)]
        down = [['y' for _ in range(3)] for _ in range(3)]
        front = [['r' for _ in range(3)] for _ in range(3)]
        back = [['o' for _ in range(3)] for _ in range(3)]
        left = [['g' for _ in range(3)] for _ in range(3)]
        right = [['b' for _ in range(3)] for _ in range(3)]
        method_num = int(input())
        methods = input().split()
        for method in methods:
            if method[0] == 'U':
                up = rotate(up, method[1])
                effect = [back[0][2], back[0][1], back[0][0],
                        right[0][2], right[0][1], right[0][0],
                        front[0][2], front[0][1], front[0][0],
                        left[0][2], left[0][1], left[0][0]]
                if method[1] == '+':
                    right[0][2] = effect[0]
                    right[0][1] = effect[1]
                    right[0][0] = effect[2]
                    front[0][2] = effect[3]
                    front[0][1] = effect[4]
                    front[0][0] = effect[5]
                    left[0][2] = effect[6]
                    left[0][1] = effect[7]
                    left[0][0] = effect[8]
                    back[0][2] = effect[9]
                    back[0][1] = effect[10]
                    back[0][0] = effect[11]
                elif method[1] == '-':
                    left[0][2] = effect[0]
                    left[0][1] = effect[1]
                    left[0][0] = effect[2]
                    back[0][2] = effect[3]
                    back[0][1] = effect[4]
                    back[0][0] = effect[5]
                    right[0][2] = effect[6]
                    right[0][1] = effect[7]
                    right[0][0] = effect[8]
                    front[0][2] = effect[9]
                    front[0][1] = effect[10]
                    front[0][0] = effect[11]

            elif method[0] == 'D':
                down = rotate(down, method[1])
                effect = [front[2][0], front[2][1], front[2][2],
                        right[2][0], right[2][1], right[2][2],
                        back[2][0], back[2][1], back[2][2],
                        left[2][0], left[2][1], left[2][2]]
                if method[1] == '+':
                    right[2][0] = effect[0]
                    right[2][1] = effect[1]
                    right[2][2] = effect[2]
                    back[2][0] = effect[3]
                    back[2][1] = effect[4]
                    back[2][2] = effect[5]
                    left[2][0] = effect[6]
                    left[2][1] = effect[7]
                    left[2][2] = effect[8]
                    front[2][0] = effect[9]
                    front[2][1] = effect[10]
                    front[2][2] = effect[11]
                elif method[1] == '-':
                    left[2][0] = effect[0]
                    left[2][1] = effect[1]
                    left[2][2] = effect[2]
                    front[2][0] = effect[3]
                    front[2][1] = effect[4]
                    front[2][2] = effect[5]
                    right[2][0] = effect[6]
                    right[2][1] = effect[7]
                    right[2][2] = effect[8]
                    back[2][0] = effect[9]
                    back[2][1] = effect[10]
                    back[2][2] = effect[11]
                    
            elif method[0] == 'F':
                front = rotate(front, method[1])
                effect = [up[2][0], up[2][1], up[2][2],
                        right[0][0], right[1][0], right[2][0],
                        down[0][2], down[0][1], down[0][0],
                        left[2][2], left[1][2], left[0][2]]
                if method[1] == '+':
                    right[0][0] = effect[0]
                    right[1][0] = effect[1]
                    right[2][0] = effect[2]
                    down[0][2] = effect[3]
                    down[0][1] = effect[4]
                    down[0][0] = effect[5]
                    left[2][2] = effect[6]
                    left[1][2] = effect[7]
                    left[0][2] = effect[8]
                    up[2][0] = effect[9]
                    up[2][1] = effect[10]
                    up[2][2] = effect[11]
                elif method[1] == '-':
                    left[2][2] = effect[0]
                    left[1][2] = effect[1]
                    left[0][2] = effect[2]
                    up[2][0] = effect[3]
                    up[2][1] = effect[4]
                    up[2][2] = effect[5]
                    right[0][0] = effect[6]
                    right[1][0] = effect[7]
                    right[2][0] = effect[8]
                    down[0][2] = effect[9]
                    down[0][1] = effect[10]
                    down[0][0] = effect[11]

            elif method[0] == 'B':
                back = rotate(back, method[1])
                effect = [up[0][2], up[0][1], up[0][0],
                        left[0][0], left[1][0], left[2][0],
                        down[2][0], down[2][1], down[2][2],
                        right[2][2], right[1][2], right[0][2]]
                if method[1] == '+':
                    left[0][0] = effect[0]
                    left[1][0] = effect[1]
                    left[2][0] = effect[2]
                    down[2][0] = effect[3]
                    down[2][1] = effect[4]
                    down[2][2] = effect[5]
                    right[2][2] = effect[6]
                    right[1][2] = effect[7]
                    right[0][2] = effect[8]
                    up[0][2] = effect[9]
                    up[0][1] = effect[10]
                    up[0][0] = effect[11]
                elif method[1] == '-':
                    right[2][2] = effect[0]
                    right[1][2] = effect[1]
                    right[0][2] = effect[2]
                    up[0][2] = effect[3]
                    up[0][1] = effect[4]
                    up[0][0] = effect[5]
                    left[0][0] = effect[6]
                    left[1][0] = effect[7]
                    left[2][0] = effect[8]
                    down[2][0] = effect[9]
                    down[2][1] = effect[10]
                    down[2][2] = effect[11]
                    
            elif method[0] == 'L':
                left = rotate(left, method[1])
                effect = [up[0][0], up[1][0], up[2][0],
                        front[0][0], front[1][0], front[2][0],
                        down[0][0], down[1][0], down[2][0],
                        back[2][2], back[1][2], back[0][2]]
                if method[1] == '+':
                    front[0][0] = effect[0]
                    front[1][0] = effect[1]
                    front[2][0] = effect[2]
                    down[0][0] = effect[3]
                    down[1][0] = effect[4]
                    down[2][0] = effect[5]
                    back[2][2] = effect[6]
                    back[1][2] = effect[7]
                    back[0][2] = effect[8]
                    up[0][0] = effect[9]
                    up[1][0] = effect[10]
                    up[2][0] = effect[11]
                elif method[1] == '-':
                    back[2][2] = effect[0]
                    back[1][2] = effect[1]
                    back[0][2] = effect[2]
                    up[0][0] = effect[3]
                    up[1][0] = effect[4]
                    up[2][0] = effect[5]
                    front[0][0] = effect[6]
                    front[1][0] = effect[7]
                    front[2][0] = effect[8]
                    down[0][0] = effect[9]
                    down[1][0] = effect[10]
                    down[2][0] = effect[11]

            elif method[0] == 'R':
                right = rotate(right, method[1])
                effect = [up[2][2], up[1][2], up[0][2],
                        back[0][0], back[1][0], back[2][0],
                        down[2][2], down[1][2], down[0][2],
                        front[2][2], front[1][2], front[0][2]]
                if method[1] == '+':
                    back[0][0] = effect[0]
                    back[1][0] = effect[1]
                    back[2][0] = effect[2]
                    down[2][2] = effect[3]
                    down[1][2] = effect[4]
                    down[0][2] = effect[5]
                    front[2][2] = effect[6]
                    front[1][2] = effect[7]
                    front[0][2] = effect[8]
                    up[2][2] = effect[9]
                    up[1][2] = effect[10]
                    up[0][2] = effect[11]
                elif method[1] == '-':
                    front[2][2] = effect[0]
                    front[1][2] = effect[1]
                    front[0][2] = effect[2]
                    up[2][2] = effect[3]
                    up[1][2] = effect[4]
                    up[0][2] = effect[5]
                    back[0][0] = effect[6]
                    back[1][0] = effect[7]
                    back[2][0] = effect[8]
                    down[2][2] = effect[9]
                    down[1][2] = effect[10]
                    down[0][2] = effect[11]
        for i in range(3):
            for j in range(3):
                print(up[i][j], end = '')
            print() 


if __name__ == '__main__':
    main()
