from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
        if len(cache) > cacheSize:
            cache.popleft()
    return answer