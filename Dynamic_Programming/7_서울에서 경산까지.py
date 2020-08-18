# https://programmers.co.kr/learn/courses/30/parts/12263
"""
knapsack problem (배낭 채우기 문제)
dp[i,w] = i번 째 까지의 보석으로 사이즈가 w인 배낭에 채울 수 있는 가치의 최댓값
wi : i번 째 보석의 무게, vi : i번 째 보석의 가치
-> wi > w 라면 dp[i,w] = dp[i-1,w]
아니라면 dp[i-1,w-wk] + vi 와 dp[i-1,w] 중 큰 값
따라서 이차원 리스트 선언해서 (0,0)부터 하나씩 채워주면 됨

작은거에서 찾는거보다
0부터 시작해서 큰거 채워주는게 나을 것 같음
여기선 안고르는지 고르는지의 문제가 아니고, 둘중에 어떤걸 고를지의 문제
dp[i][j] : i번째까지 여행지를 들렀을 때 // 어떤 길로 갔는지
dp[i][j]가 0이라면 이렇게 가는 방법이 없는거니까 continue로 넘겨주
"""
def solution(K,travel):
    dp = [[0]*(K+1) for i in range(len(travel))]
    dp[0][travel[0][0]] = travel[0][1]; dp[0][travel[0][2]] = travel[0][3]
    for i in range(1,len(travel)):
        for j in range(K):
            # 이 앞에까지의 여행지를 들리지 않았다면 pass
            if dp[i-1][j] == 0: continue
            # 도보로 갈 때 최대 시간 안넘는다면
            if j + travel[i][0] <= K:
                dp[i][j+travel[i][0]] = max(dp[i][j+travel[i][0]], dp[i-1][j] + travel[i][1])
            # 자전거로 갈 때 최대 시간 안넘는다면
            if j + travel[i][2] <= K:
                dp[i][j+travel[i][2]] = max(dp[i][j+travel[i][2]], dp[i-1][j] + travel[i][3])
    return max(dp[-1])
K = 1650
travel = [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]
print(solution(K,travel))
