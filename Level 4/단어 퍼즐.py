# https://programmers.co.kr/learn/courses/30/lessons/12983

def solution(strs, t):
    strs = set(strs) # 집합 쓰면 탐색 O(1)로 가능
    dp = [10**5] * (1+len(t))
    if t[0] in strs: dp[1] = 1
    
    for i in range(len(t)+1):
        for j in range(i-5,i):
            if j >= 0 and t[j:i] in strs:
                print(j,i,t[j:i])
                if j == 0: dp[i] = 1
                elif dp[j] != 10**5: dp[i] = min(dp[i], dp[j] + 1)
    print(dp)
    if dp[-1] == 10**5: return -1
    else: return dp[-1]

strs = 	["ab", "na", "n", "a", "bn"]
t =  "nabnabn"
print(solution(strs,t))
