# 이항계수 삼각형이라는 것을 봄

N, K = list(map(int, input().split()))

tri = []
for i in range(N+1):
    row = [0 for _ in range(i+1)]
    row[0] = 1
    row[i] = 1
    for j in range(1, i):
        row[j] = (tri[i-1][j-1] + tri[i-1][j]) % 10007
    tri.append(row)

print(tri[N][K])