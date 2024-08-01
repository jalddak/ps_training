n = 0

flag = False
for i in range(3):
    a = input()
    if a.isdigit() and not flag:
        n = int(a) + 3 - i
        flag = True

answer = ''
if n % 3 == 0:
    answer = 'Fizz'
if n % 5 == 0:
    answer += 'Buzz'

if answer == '':
    answer = n

print(answer)
