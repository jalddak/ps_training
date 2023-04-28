from itertools import combinations

def main():
    N, M = map(int, input().split())
    street = [list(map(int, input().split())) for _ in range(N)]
    
    houses = {}
    chickens = []
    for i in range(N):
        for j in range(N):
            if street[i][j] == 1:
                houses[(i,j)] = {} 
            elif street[i][j] == 2:
                chickens.append((i,j))

    for chicken in chickens:
        for house in list(houses.keys()):
            houses[house][chicken] = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

    chickens_list = list(combinations(chickens, M))
    
    candidates = []
    for l in chickens_list:
        min_distance_sum = 0
        for h in houses:
            min_distance = 100
            for c in l:
                min_distance = min(min_distance, houses[h][c])
            min_distance_sum += min_distance
        candidates.append(min_distance_sum)
        
    result = min(candidates)
    print(result)
    return result


if __name__ == '__main__':
    main()