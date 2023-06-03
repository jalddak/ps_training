from collections import deque

# n : 격자 길이, m : 손님 수, f : 연료량
n, m, f = list(map(int, input().split()))
# board : n * n 격자
board = [list(map(int, input().split())) for _ in range(n)]
# loca : 택시의 위치
loca = list(map(lambda x:x-1, list(map(int, input().split()))))
# ps : 손님의 출발지, 도착지 정보를 저장한 리스트
ps = [list(map(lambda x:x-1, list(map(int, input().split())))) for _ in range(m)]

# 초기설정으로 board에 모든 손님의 출발지점을 2로 표시해둔다.
for p in ps:
    board[p[0]][p[1]] = 2

# 위, 왼쪽, 아래, 오른쪽
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 최단거리의 손님을 찾는 함수
def find(board, loca, ps):
    global n, m, f, dy, dx

    # visted : 한번 택시가 방문했던 곳은 다시 방문하지 않게 하기 위함
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # queue : [y, x, distance] 형식을 가진 리스트
    # y : row 위치 / x : col 위치 / distance : y, x 까지 이동하기 위해 택시가 이동한 거리
    queue = deque([loca[:] + [0]])
    # short : 손님과의 최단거리
    short = f
    # human : 최단거리의 손님 위치
    human = []

    # 택시의 출발지점이 손님위치와 같은 경우
    if board[loca[0]][loca[1]] == 2:
        human = loca[:]
        short = 0
    
    else:
        # 큐가 다 비워질 때 까지 확인.
        while len(queue) != 0:
            # y : row 위치 / x : col 위치 / distance : y, x 까지 이동하기 위해 택시가 이동한 거리
            y, x, distance = queue.popleft()
            # 택시의 위치가 short와 같거나 크다면, 이 이상 움직여도 의미가 없다. 이미 더 짧은 거리에 가능한 손님이 있기 때문
            # 만약 short 가 f 즉, 연료인 상황이라면 이미 연료를 다 써서 이동한 곳이 y, x 이기 때문에 더이상 움직일 수 없다.
            if distance < short:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    # board의 범위 안에 들어오면서, 벽이 아니고, 방문한 적이 없던 곳이라면
                    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1 and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        # 만약 이동가능 한 위치에 손님이 있는 경우
                        if board[ny][nx] == 2:
                            # 우선 최단거리를 갱신해준다.
                            short = distance + 1
                            # 만약 최단거리 손님을 먼저 발견했었다면
                            if len(human) != 0:
                                # 행의 위치가 더 작은 쪽을 우선으로
                                if human[0] > ny:
                                    human = [ny, nx]
                                # 행의 위치가 같다면 열의 위치가 더 작은 쪽을 우선으로
                                elif human[0] == ny and human[1] > nx:
                                    human = [ny, nx]
                            # 최단거리 손님을 발견한적 없었다면
                            else:
                                human = [ny, nx]
                        # 이동가능 한 위치에 손님이 없으면 큐에 해당 위치와 이동거리 정보를 삽입
                        else:
                            queue.append([ny, nx, distance + 1])

    # pinfo : 최단 거리 손님의 정보 (출발지, 목적지)
    pinfo = []
    # 만약 최단 거리 손님이 존재한다면
    if len(human) != 0:
        for p in ps:
            # 손님의 출발지, 목적지 정보를 담은 리스트에서 해당 손님의 정보를 찾아내고, 그 손님은 ps리스트에서 지운다.
            if human == [p[0], p[1]]:
                i = ps.index(p)
                pinfo = ps.pop(i)
                break
    #손님 정보와 최단거리까지 이동하는데 사용한 연료를 return 한다.
    return pinfo, short

# 손님을 목적지 까지 데려다 주는 함수
def arrive(board, p):
    global n, m, f, dy, dx

    # # visted : 한번 택시가 방문했던 곳은 다시 방문하지 않게 하기 위함
    # queue : [y, x, distance] 형식을 가진 리스트
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([[p[0], p[1], 0]])
    # result : 손님이 목적지에 도착했는지 여부
    result = False
    
    # queue가 비워지거나 손님이 목적지에 도착할 때 가지 루프
    while len(queue) != 0 and not result:
        # y : row 위치 / x : col 위치 / distance : y, x 까지 이동하기 위해 택시가 이동한 거리
        y, x, distance = queue.popleft()
        # 만약 이동거리가 연료와 같아진다면 그 이상은 이동이 불가능함
        if distance < f:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # board의 범위 안에 들어오면서, 벽이 아니고, 방문한 적이 없던 곳이라면
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append([ny, nx, distance+1])
                    # 만약 이동가능 한 위치가, 손님의 목적지와 같다면
                    if [ny, nx] == [p[2], p[3]]:
                        # 목적지에 도착한다면, 손님의 출발지부터 목적지까지 사용했던 연료의 두배만큼 채워지기 때문에 굳이 빼지않고 이동한 거리만큼 더해줬다.
                        f += (distance + 1)
                        # 도착했으므로, result는 True
                        result = True
                        break
    return result


def main():
    global n, m, f, dy, dx, board, loca, ps

    # 손님이 게속 존재하고, 연료가 0보다 크다면 게속 루프를 돈다.
    while len(ps) != 0 and f > 0:
        # p : 최단 거리의 손님, use : 해당 손님의 위치까지 가는데 사용한 연료의 양
        p, use = find(board, loca, ps)
        # 만약 최단거리 손님을 찾지 못한 경우 -1 출력하고 끝낸다. (연료가 바닥나거나 벽에 막혀 손님을 찾을 수 없는 경우라고 생각함.)
        if len(p) == 0:
            print(-1)
            return
        # 그렇지 않다면, 택시의 현재위치를 손님의 위치로 바꿔주고, board에서 손님은 태웠으니 2->0 으로 바꿔주고, 연료는 사용량만큼 줄여준다.
        loca = [p[0], p[1]]
        board[p[0]][p[1]] = 0
        f -= use

        # 손님이 목적지에 도착한 경우, 택시의 현재 위치는 손님의 목적지가 된다.
        if arrive(board, p):
            loca = [p[2], p[3]]
        # 손님을 목적지에 데려다주지 못한 경우(연료를 모두 사용하거나, 벽에 막힌 경우로 생각됨), -1 출력하고 멈춤
        else:
            print(-1)
            return
        
    print(f)



if __name__ == '__main__':
    main()