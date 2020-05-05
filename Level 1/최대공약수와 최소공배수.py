#https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(n,m):
    if m == 0:
        return n
    return gcd(m,n%m)

def solution(n,m):
    n,m = max(n,m), min(n,m)
    g = gcd(n,m)
    return [g, n*m//g]

print(solution(3,12))
