#https://programmers.co.kr/learn/courses/30/lessons/42896
"""
가장 마지막 칸부터 역방향으로 탐색해주기
left[i] > right[j]이라면 dp[i,j] = dp[i,j+1] + right[j]
아니라면 dp[i,j] = max(dp[i+1,j], dp[i+1,j+1])
"""
def solution(left,right):
    dp = [[0] * (1+len(left)) for _ in range(1+len(right))]
    
    for i in range(len(left)-1,-1,-1):
        for j in range(len(right)-1,-1,-1):
            if left[i] > right[j]:
                dp[i][j] = dp[i][j+1] + right[j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
    #print(dp)
    return dp[0][0]

def s(left,right):
    dp = [[0] * (1+len(left)) for _ in range(1+len(right))]
    
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i] > right[j]:
                dp[i+1][j+1] = dp[i+1][j] + right[j]
            else:
                dp[i+1][j+1] = max(dp[i][j], dp[i][j+1])
    print(dp)
    return dp[0][0]

left = [3,2,5]
right = [2,4,1]
print(solution(left,right))
left = [3,3,1]
right = [7,7,1]
print(s(left,right))
