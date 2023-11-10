"""
N X M 크기의 직사각형 격자판이 있다. 격자판의 각 칸은 1 x 1 크기의 정사각형 모양이다. 
당신은 이 격자판의 각 칸을 검은색 또는 흰색으로 칠할 계획이다.
당신은 격자판의 칸 중 몇 개(0개 이상 NM개 이하)는 검은색으로 칠할지 흰색으로 칠할지를 이미 정해 놓았다. 
정확히 표현하자면, N X M 크기의 행렬 A가 있어서, 
Ai,j 가 ‘#’라면 격자판의 i행 j열에 있는 칸은 검은색으로 칠해야 하고, 
Ai,j 가 ‘.’라면 격자판의 i행 j열에 있는 칸은 흰색으로 칠해야 하며, 
Ai,j 가 ‘?’라면 격자판의 i행 j열에 있는 칸은 검은색으로 칠해도 되고 흰색으로 칠해도 된다.
당신은 아직 색이 정해지지 않은 칸들을 어떤 색으로 칠할지를 잘 정한 뒤 격자판을 색칠할 것이다. 
색칠한 결과 격자판의 인접한 (즉, 변 하나를 공유하는) 두 칸의 색이 항상 다르게 할 수 있는지를 판단하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N과 M(1 ≤ N ≤50, 1 ≤ M ≤ 50)이 공백 하나를 사이로 두고 주어진다. 
다음 N개의 줄에는 '#', '.', '?'로만 구성된 길이가 M인 문자열이 하나씩 주어지며, 이는 행렬 A를 나타낸다.

[출력]
각 테스트 케이스마다, '?'에 해당하는 칸의 색을 잘 정하여, 
격자판의 인접한 두 칸의 색이 항상 서로 다르게 할 수 있다면 ‘possible’을, 
그렇지 않다면 ‘impossible’을 출력한다.
"""
import sys
input = sys.stdin.readline
T = int(input())

dy = [0, 1]
dx = [1, 0]

for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    check = True

    cnt = 0
    candidate = ['#', '.']
    if board[0][0] == '?':
        cnt += 1

    while cnt >= 0:
        check = True
        copy = []
        for i in range(N):
            copy.append(board[i][:])
        if board[0][0] == '?':
            copy[0][0] = candidate[cnt]
        cnt -= 1
        for i in range(N):
            for j in range(M):
                for d in range(2):
                    cy = i + dy[d]
                    cx = j + dx[d]
                    if 0 <= cy < N and 0 <= cx < M:
                        if copy[cy][cx] != copy[i][j]:
                            if copy[cy][cx] == "?":
                                if copy[i][j] == '#':
                                    copy[cy][cx] = "."
                                else:
                                    copy[cy][cx] = '#'
                        else:
                            check = False
                            break
                if not check:
                    break
            if not check:
                break
        if check:
            break
    if check:
        print("#" + str(t) + " possible")
    else:
        print("#" + str(t) + " impossible")