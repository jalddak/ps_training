# combination 반갈죽 특징 : 반반으로 정 반대되게 매핑되는 것 같다.

from itertools import combinations

n = int(input())
s = []
h = []
for i in range(n):
    s.append(list(map(int, input().split())))
    h.append(i)
    
result = 100 * n * n

def synerge(team):
    sum = 0
    length = len(team)
    for i in range(length):
        for j in range(i+1, length):
            sum += s[team[i]][team[j]] + s[team[j]][team[i]]
    return sum


def main():
    global h, result
    half = list(combinations(h, n//2))
    
    for i in range(len(half)//2):
        start = half[i]
        link = half[-1-i]
        result = min(result, abs(synerge(list(start)) - synerge(list(link))))

if __name__ == '__main__':
    main()
    print(result)