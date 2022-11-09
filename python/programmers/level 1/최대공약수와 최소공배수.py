def solution(n, m):
    nlist = []
    mlist = []
    최대공약수요소 = []
    최대공약수 = 1
    최소공배수 = n * m
    
    n_copy = n
    m_copy = m
    
    temp = 2
    while n != 1:
        if n % temp == 0:
            nlist.append(temp)
            n = n // temp
            temp = 2
        else:
            temp += 1
    
    temp = 2
    while m != 1:
        if m % temp == 0:
            mlist.append(temp)
            m = m // temp
            temp = 2
        else:
            temp += 1
    
    for num in nlist:
        if num in mlist:
            mlist.remove(num)
            최대공약수요소.append(num)
    
    for num in 최대공약수요소:
        최대공약수 *= num
            
    최소공배수 = 최대공약수 * (n_copy // 최대공약수) * (m_copy // 최대공약수)
    
    answer = [최대공약수, 최소공배수]
    return answer