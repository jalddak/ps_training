n = int(input())

answer = 0
if ((n % 4 == 0 and n % 100 != 0) or n % 400 == 0): 
    answer = 1
print(answer)