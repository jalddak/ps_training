# dictionary 를 사용해서 필요부분만 체크하는 식으로 하려 했는데 그것 보다 그냥 다 도는게 더 빨랐다.
# dictionary 와 뭔가 메모리적인 차이가 있는 것 같은데...
# 파이썬을 잘 아는건 아니지만, list가 C에서의 vector 형식이라면 list가 더 빠르게 접근할 수 있습니다. 둘 다 접근시 O(1)이지만 hash는 데이터가 많아짐에 따라 복잡도가 올라가니 접근 속도는 list가 더 빠르겠죠. 
# hash는 접근 속도 목적보다는 입력 인덱스가 너무 넓게 분산되어 있을 때 list로 모든 공간을 할당하면 메모리가 너무 커지기 때문에 사용하는 경우가 많습니다.
# 라는 질문에 대한 답이 있는걸 보긴 봄

from collections import deque

def main():
    N, M, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    land = [[5 for _ in range(N)] for _ in range(N)]
    trees = [[deque([]) for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        y, x, old = map(int,input().split())
        trees[y-1][x-1].append(old)

    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for _ in range(k):
        # 봄 + 여름
        for i in range(N):
            for j in range(N):
                for k in range(len(trees[i][j])):
                    if land[i][j] >= trees[i][j][k]:
                        land[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        for _ in range(k, len(trees[i][j])):
                            land[i][j] += trees[i][j].pop() // 2
                        break
        # 가을
        for i in range(N):
            for j in range(N):
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] % 5 == 0:
                        for l in range(8):
                            around_y = i + dy[l]
                            around_x = j + dx[l]
                            if around_y >= 0 and around_y < N and around_x >= 0 and around_x < N:
                                trees[around_y][around_x].appendleft(1)

        # 겨울
        for i in range(N):
            for j in range(N):
                land[i][j] += A[i][j]

    tree_count = 0
    for i in range(N):
        for j in range(N):
            tree_count += len(trees[i][j])
    print(tree_count)
    return tree_count
    

if __name__ == '__main__':
    main()