# https://programmers.co.kr/learn/courses/30/lessons/12942
"""
2차원 dp 선언하기
dp[i][j] : i부터 j까지의 연산횟수의 최솟값
dp[i][j] = max(dp[i][k]+dp[k+1][j]+matrix[i][0] * matrix[k][1] * matrix[j][1])
k = i~j-1까지
i == j -> dp[i][j] = 0
"""

def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[10**9]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 0
    # i+j의 거리가 작은 것부터 dp 돌려줘야 함
    for d in range(1,n):
        for i in range(n-d):
            j = i + d
            m = 10**9
            for k in range(i,j):
                m = min(m, dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
            dp[i][j] = m
    return dp[0][-1]

print(solution([[5,3],[3,10],[10,6]]))
