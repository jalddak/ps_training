import heapq

arr = [9, 2, 1, 8, 100, 50]
heap = []

for n in arr:
	heapq.heappush(heap, (-n, n))

print(heap)
print()

while len(heap) != 0:
	n = heapq.heappop(heap)
	print(heap, n[1])