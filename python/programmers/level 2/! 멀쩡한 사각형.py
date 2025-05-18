def calc_gcd(w, h):
    if w < h:
        w, h = h, w
    if w % h == 0:
        return h
    else:
        return calc_gcd(h, w%h)

def solution(w,h):
    gcd = calc_gcd(w, h)
    answer = w*h - gcd * ((w//gcd) + (h//gcd) - 1)
    return answer