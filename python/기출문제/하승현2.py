def main(goods):
    result = []

    for good in goods:
        length = len(good)
        check = []
        for i in range(length):
            for j in range(length - i):
                sub = good[j:j+i+1]
                cnt = 0
                for temp in goods:
                    if sub in temp:
                        cnt += 1
                        if cnt > 1:
                            break
                if cnt == 1:
                    if sub not in check:
                        check.append(sub)
            if len(check) != 0:
                string = ''
                for i in range(len(check)):
                    string += check[i]
                    if i != len(check)-1:
                        string += ' '
                result.append(string)
                break
        if len(check) == 0:
            result.append('None')
    print(result)
    return result

goods = ["pencil", "cilicon", "contrabase", "picturelist"]
main(goods)
goods = ["abcdeabcd", "cdabe", "abce", "bcdeab"]
main(goods)