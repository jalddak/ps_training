answer = []

for tc in range(1, 11):
    sb = "#" + str(tc) + " "
    length = int(input())

    stack = []
    pair = {'>' : '<', '}' : '{', "]" : "[", ")" : "("}
    left = set(pair.values())
    right = set(pair.keys())

    string = input()
    
    result = 1
    for i in range(length):
        if string[i] in left:
            stack.append(string[i])
        else:
            if stack[-1] == pair[string[i]]:
                stack.pop()
            else:
                result = 0
                break
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)
