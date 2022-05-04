import numpy as np

n = 3

for i in range(n, 0, -1):
    print(i, end = ' ')
print()

for i in range(n):
    print(i, end = ' ')
print()

for i in range(1, n):
    print(i, end = ' ')
print()

for i in range(1, n, 1):
    print(i, end = ' ')
print()

for i in range(n, 0, -1):
    print(i, end = ' ')
print()

arr = np.arange(0,12)
print(arr)
arr = arr.reshape(4,3)
print(arr)
arr = arr.reshape(len(arr) * len(arr[0]))
print(arr)