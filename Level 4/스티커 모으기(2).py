# https://programmers.co.kr/learn/courses/30/lessons/12971
"""
dp[i] = max(sticker[i]+dp[i-2],sticker[i]+dp[i-3],dp[i-1])
(0,1,2) 중 하나는 반드시 고르니까 세가지 케이스 확인하기
"""

def solution(sticker):
    if len(sticker) <= 3: return max(sticker)
    dp1 = [0] * len(sticker)
    dp1[2] = sticker[2]
    dp2 = [0] * len(sticker)
    dp2[1] = dp2[2] = sticker[1]
    dp3 = [0] * len(sticker)
    dp3[0] = dp3[1] = dp3[2] = sticker[0]
    dp3[2] += sticker[2]
    for i in range(3,len(dp1)):
        dp1[i] = max(sticker[i]+dp1[i-2], sticker[i]+dp1[i-3], dp1[i-1])
        dp2[i] = max(sticker[i]+dp2[i-2], sticker[i]+dp2[i-3], dp2[i-1])
        dp3[i] = max(sticker[i]+dp3[i-2], sticker[i]+dp3[i-3], dp3[i-1])
    dp3[-1] = max(dp3[i-1],dp3[i-2],dp3[i-3])
    print(dp1)
    print(dp2)
    print(dp3)
    return max(dp1[-1],dp2[-1],dp3[-1])

    
print(solution([14,6,5,11,3,9,2,10]))
