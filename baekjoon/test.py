# combinations 를 활용한다.
from itertools import combinations

arr = [1,2,3,4,5]
# 리스트 요소를 부분집합으로 나누는 방법
list_2 = list(combinations(arr, 2))

# 안에 들어가 있는 요소의 타입은 tuple 형태이다.
print(list_2, type(list_2[0]))

# 집합으로 사용하기 편하려면 set으로 데이터 타입을 바꿔준다.
print(set(list_2[0]))

# 교집합, 차집합, 합집합 정리

set1 = set({1,2,3})
set2 = set({2,3,4})
set3 = set({4,5,6})

print(set1 & set2)
print(set1.intersection(set2))
print(set1 & set3)

set1 = set({1,2,3})
set2 = set({2,3,4})
set3 = set({4,5,6})

print(set1 - set2) # {1}
print(set1.difference(set2)) # {1}
print(set1 - set3) # {1, 2, 3}

set1 = set({1,2,3})
set2 = set({2,3,4})
set3 = set({4,5,6})

print(set1 | set2) # {1, 2, 3, 4}
print(set1.union(set2)) # {1, 2, 3, 4}
print(set1 | set3) # {1, 2, 3, 4, 5, 6}

count = 5
for i in range(1,count):
    print(i)
    count += 1

a = [['w' for _ in range(3)] for _ in range(3)]
e = [a[0][0]]
print(e, a)
a[0][0] = 'a'
print(e, a)