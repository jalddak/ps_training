import sys
input = sys.stdin.readline

ori = list(map(int, input().split()))
if ori == sorted(ori):
    print("ascending")
elif ori == sorted(ori, reverse=True):
    print("descending")
else:
    print("mixed")