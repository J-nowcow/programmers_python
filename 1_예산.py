#https://programmers.co.kr/learn/courses/30/lessons/43237
"""
지방의 수 10만 이하 -> nlogn 이하로 해결해야 함
정렬해놓고 이분 탐색으로 값 찾아주면 됨
"""

def solution(budgets, M):
    budgets.sort()
    begin = 0; end = max(budgets) # 하나도 수용 못하는 경우 있어서 0으로 설
    if sum(budgets) <= M: # 전부 수용 가능할 때 
        return end
    
    while begin <= end: # 아니라면 탐색해주기
        mid = (begin+end)//2
        money = 0
        for i in range(len(budgets)):
            if budgets[i] < mid: # 상한액보다 작으면
                money += budgets[i]
            else: # 아니면
                money += mid * (len(budgets)-i) # 나머지 다 상한액으로 넣어주기
                break
        if money == M: break # 같으면 바로 종료
        elif money < M: # 예산 초과 안했으면
            begin = mid + 1
        else: # 했으면
            end = mid - 1
    return end

budgets = [120,110,140,150]
M = 485
print(solution(budgets, M))
