#https://programmers.co.kr/learn/courses/30/lessons/12921
"""
에라토스테네스 체 구현하기
set으로 구현하면 O(1)에 빼기 연산 가능해서 좀 더 쉽게 가능, 시간도 더 빠름
"""
"""
def solution(n):
    a = [2]
    for i in range(3,n+1):
        for j in a:
            if i % j == 0: break
            elif i < j**2: a.append(i); break
    return len(a)
"""
def solution(n):
    num = set(range(2,n+1))
    for i in range(2,n//2+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

print(solution(5))
