# https://programmers.co.kr/learn/courses/30/lessons/42895
"""
dp[8] 각각에 집합 정의해놓기: dp[k] = k개의 숫자로 만들 수 있는 수들의 집합
각 집합에 1, 11, 111, 1111, ... default 설정
n개의 숫자로 만들기 : n-1,1 + n-2,2 + ... + 1,n-1
가능한 방법: a+b, a-b, a*b, a//b (b가 0이 아니라면)
"""

def solution(N, number):
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    for i in range(8):
        for j in range(i):
            for a in dp[j]:
                for b in dp[i-j-1]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0 : dp[i].add(a//b)
        if number in dp[i]: return i+1
    return -1

print(solution(5,12))
