def solution(n, wires):
    wires.sort(key=lambda x: (x[0], x[1]))
    answer = n
    for i in range(n-1):
        left = wires[i][0]
        right = wires[i][1]
        bundle = []
        for j in range(n-1):
            if j == i:
                continue
            if len(bundle) == 0:
                bundle.append(wires[j])
                continue
            insertion = False
            for index in range(len(bundle)):
                if len(set(bundle[index]) & set(wires[j])) != 0:
                    bundle[index] = list(set(bundle[index]) | set(wires[j]))
                    insertion = True
                    break
            if insertion == False:
                bundle.append(wires[j])
        if len(bundle) > 1:
            index = 0
            while index < len(bundle)-1:
                plus = 1
                while (index + plus) < len(bundle):
                    if len(set(bundle[index]) & set(bundle[index+plus])) != 0:
                        bundle[index] = list(set(bundle[index]) | set(bundle[index+plus]))
                        bundle.pop(index+plus)
                        plus = 1
                        continue
                    plus += 1
                index += 1
        
        print(left, right, bundle)
        
        result = 0
        if len(bundle) > 1:
            result = abs(len(bundle[0]) - len(bundle[1]))
        else:
            result = n-2
            
        if answer > result: 
            answer = result
            
        
    return answer