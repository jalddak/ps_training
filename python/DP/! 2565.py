# LIS 알고리즘

# O(N**2) 시간 복잡도
n = int(input())

wires = [list(map(int, input().split())) for _ in range(n)]
wires.sort(key = lambda x: (x[0], x[1]))

length = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if wires[j][1] < wires[i][1]:
            length[i] = max(length[i], length[j]+1)

print(n - max(length))


# O(nlogn) 시간 복잡도
n = int(input())

wires = [list(map(int, input().split())) for _ in range(n)]
wires.sort(key = lambda x: (x[0], x[1]))

lis = [wires[0][1]]
def main():
    global n, wires, lis
    for i in range(1, n):
        if wires[i][1] < lis[-1]:
            binarySearch(0, len(lis)-1, wires[i][1])
        else:
            lis.append(wires[i][1])
    print(n - len(lis))

def binarySearch(left, right, wire):
    global lis
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < wire:
            left = mid + 1
        else:
            right = mid
    
    lis[right] = wire

if __name__ == '__main__':
    main()