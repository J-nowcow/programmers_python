#https://programmers.co.kr/learn/courses/30/lessons/43105

"""
삼각형 한 줄씩 내려가면서 더해주고, 최댓값 출력해주면 됨
얘도 왜 level 3... DP가 어렵다는 편견이 있어서 그런건지 아님 파이썬이 DP가
너무 쉽게 구현돼서 쉬운건지....
"""

def solution(triangle):
    dp = [triangle[0][0]]
    for i in triangle[1:]:
        dp = [dp[0]+i[0]] + [max(dp[j-1]+i[j], dp[j]+i[j]) for j in range(1,len(i)-1)] + [dp[-1]+i[-1]]
    return max(dp)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
