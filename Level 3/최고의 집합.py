# https://programmers.co.kr/learn/courses/30/lessons/12938
"""
전체 집합의 개수 n개
각 원소: s // n
남은 s % n 나머지에 재분배
s//n: n - s%n개, s//n+1: s%n개 
"""
solution = lambda n,s: [[s//n] *(n-s%n) + [s//n+1] * (s%n),[-1]][s<n]
print(solution(2,9))
