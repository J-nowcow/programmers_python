# https://programmers.co.kr/learn/courses/30/lessons/42898
"""
물이 없는 칸이라면 경우의 수 = 윗칸 + 왼쪽칸 경우의 수
0,0 빈 리스트 하나 만들어주면 예외처리 간단해짐
웅덩이 (m,n)으로 들어오기 때문에 (n,m)으로 판별해주기
최단거리가 m+n-3이 아닌 경우도 있는데 이 경우를 고려해주면 시간복잡도가 터짐
(문제 조건이 추가로 필요함)
"""

def solution(m, n, puddles):
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] in puddles: pass
            else: dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
            if i == 1 and j == 1: dp[1][1] = 1 # 첫칸 1로 default 설정
    return dp[-1][-1] 

print(solution(4,3,[[2,2]]))
